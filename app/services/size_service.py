from typing import List
from warnings import catch_warnings

from app.schemas.bodyMeasurments import BodyMeasurments
from app.schemas.productMeasuerment import ProductMeasurment
from app.schemas.sizeConstraint import SizeConstraint
from app.schemas.sizeFit import SizeFit

comfort_score = {
    "ADJUSTED":5,"LOOSE":3,"TIGHT":3,"TOO_LOOSE":1,"TOO_TIGHT":1,"UNKNOWN":0
}

def classify_fit(user_val, min_v, max_v):
    if min_v is None or max_v is None:
        return "UNKNOWN"
    if user_val < min_v * 0.95: return "TOO_LOOSE"
    if user_val < min_v: return "LOOSE"
    if min_v <= user_val <= max_v: return "ADJUSTED"
    if user_val <= max_v * 1.05: return "TIGHT"
    return "TOO_TIGHT"

def score_comfort(comfort_dict):
    if(len(comfort_dict)==0) :
        return 0

    return sum(comfort_score.get(v,0) for v in comfort_dict.values()) / len(comfort_dict)

def recomanded_fit(bodyMeasurments :BodyMeasurments, sizesConstraint: List[SizeConstraint] ):
    sizesFit : List[SizeFit] = []

    for sc in sizesConstraint:
        sizeFit=SizeFit()
        comfort={}
        try :
            for measurement in sc.measurements:
                user_value = getattr(bodyMeasurments, measurement.measurementName)
                fit_class = classify_fit(user_value, measurement.minValue, measurement.maxValue)
                comfort[measurement.measurementName] = fit_class
        except Exception as e:
            print("Error happened:", e)
        sizeFit.comfort = comfort
        sizeFit.SizeName = sc.sizeName
        sizeFit.SizeOrder = sc.sizeOrder
        sizeFit.score = score_comfort(comfort)
        sizesFit.append(sizeFit)
    a=sorted(sizesFit, key=lambda x: x.score, reverse=True)
    print ("-------------------------the vector a sorted -------------------------------")
    print(a)
    print("-------------------------------------------------------------------------------")
    return a


def main():
    # Sample body measurements
    user_body = BodyMeasurments(
        height=175,
        weight=70,
        gender="male",
        ArmLength=60,
        Chest=95,
        Hips=90,
        Inseam=80,
        InseamFloor=85,
        LegContour=50,
        ShoulderSpan=45,
        Waist=80,
        Underchest=0
    )

    # Sample size constraints
    sizes_constraints = [
        SizeConstraint(
            sizeName="Small",
            sizeOrder=1,
            measurements=[
                ProductMeasurment(measurementName="Chest", minValue=88,maxValue= 94),
                ProductMeasurment(measurementName="Waist", minValue=75, maxValue=80)
            ]
        ),
        SizeConstraint(
            sizeName="Medium",
            sizeOrder=2,
            measurements=[
                ProductMeasurment(measurementName="Chest",minValue=95, maxValue=100),
                ProductMeasurment(measurementName="Waist", minValue=81, maxValue=85)
            ]
        ),
        SizeConstraint(
            sizeName="Large",
            sizeOrder=3,
            measurements=[
                ProductMeasurment(measurementName="Chest", minValue=101,maxValue= 110),
                ProductMeasurment(measurementName="Waist", minValue=86, maxValue=95)
            ]
        )
    ]

    # Run recommendation
    recommended_sizes = recomanded_fit(user_body, sizes_constraints)

    # Print results
    for size in recommended_sizes:
        print(f"Size: {size.SizeName}, Score: {size.score}, Comfort: {size.comfort} , SIzeOrder {size.SizeOrder}")

if __name__ == "__main__":
    main()