from typing import List

import public
from pydantic import BaseModel

from app.schemas.bodyMeasurments import BodyMeasurments
from app.schemas.sizeConstraint import SizeConstraint
from app.schemas.sizeFit import SizeFit


class GetRecommendedSizeResponse(BaseModel):
    comfort: List[SizeFit]
    sizing_chart_info : List[SizeConstraint]
    user_measurements : BodyMeasurments