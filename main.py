from fastapi import FastAPI
from app.api.main import router as main_router
from app.api.genai import router as genai_router
from app.api.ml import router as ml_router

app = FastAPI(title="Mentor Search")
app.include_router(main_router)
app.include_router(genai_router, prefix="/genai")
app.include_router(ml_router, prefix="/ml")
