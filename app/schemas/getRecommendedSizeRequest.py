from pydantic import BaseModel

from app.schemas.bra import Bra
from typing import Optional


class GetRecommendedSizeRequest(BaseModel):
    height: float
    weight: float
    age: float
    gender: str
    body_shape:str
    product_id: str
    bra: Optional[Bra] = None
