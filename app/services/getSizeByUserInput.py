from app.schemas.getRecommendedSizeResponse import GetRecommendedSizeResponse
from app.services.measure_service import getBodyMeasurements
from app.services.product_service import getSizeConstraintsByProductId
from app.services.size_service import recomanded_fit


def getSizeByUserInput(input):
    bodyMeasrements=getBodyMeasurements(input)
    sizeConstraints=getSizeConstraintsByProductId(1)
    response=GetRecommendedSizeResponse(comfort=recomanded_fit(bodyMeasrements,sizeConstraints),
                                        sizing_chart_info=sizeConstraints,
                                        user_measurements=bodyMeasrements)
    return response