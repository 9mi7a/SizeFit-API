from pydantic import BaseModel

class Bra(BaseModel):
    region: str
    band: float
    cup: str
