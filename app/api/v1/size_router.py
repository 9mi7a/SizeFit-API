from fastapi import APIRouter
from app.schemas.getRecommendedSizeRequest import GetRecommendedSizeRequest
from app.services.getSizeByUserInput import getSizeByUserInput
from app.services.size_service import recomanded_fit

router = APIRouter()

@router.post("/recommend")
def size_recommendation(data: GetRecommendedSizeRequest):
    result = getSizeByUserInput(data)
    print(result)
    return result
