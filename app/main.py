from fastapi import FastAPI
from app.routers import analyze

app = FastAPI()

app.include_router(analyze.router)

@app.get("/")
def root():
    return {"message": "Repo Analyzer API is running"}
