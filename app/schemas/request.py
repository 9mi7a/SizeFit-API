from pydantic import BaseModel

class SizeRequest(BaseModel):
    height: float
    weight: float
    age: int
    gender: str
    product_id: str
