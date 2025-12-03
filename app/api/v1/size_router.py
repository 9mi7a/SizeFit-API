from fastapi import APIRouter
from app.schemas.request import SizeRequest
from app.services.size_service import recommend_size

router = APIRouter()

@router.post("/recommend")
def size_recommendation(data: SizeRequest):
    result = recommend_size(data)
    return result
