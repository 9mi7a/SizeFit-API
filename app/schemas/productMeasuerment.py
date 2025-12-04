from pydantic import BaseModel

class ProductMeasurment(BaseModel):
    measurementName: str
    minValue: float
    maxValue: float
