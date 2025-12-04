import public
from pydantic import BaseModel

class BodyMeasurments(BaseModel):
    height: float=0
    weight: float=0
    # gender: str=""
    ArmLength: float=0
    Chest: float=0
    Hips: float=0
    Inseam: float=0
    InseamFloor: float=0
    LegContour:float=0
    ShoulderSpan:float=0
    Waist: float=0
    # if female###################
    Underchest: float=-1