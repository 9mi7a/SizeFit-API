from typing import Dict
from pydantic import BaseModel

class SizeFit(BaseModel):
    SizeName: str =""
    SizeOrder: int =0
    comfort: Dict[str, str] ={}
    score: float =0.0