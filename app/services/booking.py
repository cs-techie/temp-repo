import uuid
from ..utils.redis_client import get_redis
from ..config import settings
from sqlalchemy.orm import Session
from ..models import Mentor
from ..database import SessionLocal

LOCK_TTL_MS = settings.LOCK_TTL_MS

async def acquire_lock(redis, lock_key: str, ttl_ms: int = LOCK_TTL_MS):
    token = str(uuid.uuid4())
    ok = await redis.set(lock_key, token, nx=True, px=ttl_ms)
    return token if ok else None

async def release_lock(redis, lock_key: str, token: str):
    lua = """
    if redis.call("get", KEYS[1]) == ARGV[1] then
      return redis.call("del", KEYS[1])
    else
      return 0
    end
    """
    return await redis.eval(lua, 1, lock_key, token)

async def book_slot(mentor_id: int, slot_id: str):
    redis = await get_redis()
    lock_key = f"slot:{mentor_id}:{slot_id}:lock"
    token = await acquire_lock(redis, lock_key)
    if not token:
        return {"ok": False, "reason": "locked"}

    # double-check DB
    db: Session = SessionLocal()
    try:
        mentor = db.query(Mentor).filter(Mentor.id == mentor_id).first()
        if not mentor:
            return {"ok": False, "reason": "not_found"}
        availability = mentor.availability or []
        for s in availability:
            if s.get("slot_id") == slot_id:
                if s.get("is_booked"):
                    return {"ok": False, "reason": "already_booked"}
                s["is_booked"] = True
                mentor.availability = availability
                db.add(mentor)
                db.commit()
                # update ES index asynchronously (simpler: call update here)
                from ..services.indexer import update_availability
                update_availability(str(mentor_id), availability)
                return {"ok": True}
        return {"ok": False, "reason": "slot_not_found"}
    finally:
        await release_lock(redis, lock_key, token)
        db.close()
