from typing import List

from pydantic import BaseModel

from app.schemas.productMeasuerment import ProductMeasurment


class SizeConstraint(BaseModel):
    sizeName: str
    sizeOrder: int
    measurements: List[ProductMeasurment]