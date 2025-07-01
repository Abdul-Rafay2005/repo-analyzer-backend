from fastapi import APIRouter, HTTPException
from app.models.input_model import AnalyzeRequest

router = APIRouter()

@router.post("/analyze")
async def analyze_repo(input_data: AnalyzeRequest):
    # For now, just echo back the input
    return {
        "status": "received",
        "type": input_data.input_type,
        "value": input_data.value
    }
