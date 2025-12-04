from app.schemas.bodyMeasurments import BodyMeasurments
from app.services.ml_service import predict


def getBodyMeasurements(input):
    bodyMeasurments = BodyMeasurments()
    for field_name in bodyMeasurments.dict().keys():
        if field_name in {"height","weight","gender"}:
            continue
        setattr(bodyMeasurments, field_name, predict(field_name, input))
    bodyMeasurments.height=input.height
    bodyMeasurments.weight=input.weight
    return bodyMeasurments