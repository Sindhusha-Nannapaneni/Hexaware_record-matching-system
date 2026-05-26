from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from src.matcher import RecordMatcher

app = FastAPI()

matcher = RecordMatcher()


class MatchRequest(BaseModel):
    crm_record: Dict[str, Any]
    calendar_record: Dict[str, Any]


@app.post("/match")
def predict_match(request: MatchRequest):

    try:

        result = matcher.calculate_match(
            request.crm_record,
            request.calendar_record
        )

        return {
            "match": result["match"],
            "confidence": round(result["confidence"], 3)
        }

    except Exception as e:

        return {
            "error": str(e)
        }