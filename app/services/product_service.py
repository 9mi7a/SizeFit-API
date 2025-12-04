from typing import List

from app.schemas.productMeasuerment import ProductMeasurment
from app.schemas.sizeConstraint import SizeConstraint


def getSizeConstraintsByProductId(productId):
    return [SizeConstraint(
        sizeName="34",
        sizeOrder=0,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=162.0, maxValue=165.0),
            ProductMeasurment(measurementName="Hips", minValue=83.0, maxValue=86.0),
            ProductMeasurment(measurementName="Waist", minValue=66.0, maxValue=72.0),
        ]
    ),

    SizeConstraint(
        sizeName="36",
        sizeOrder=1,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=162.0, maxValue=165.0),
            ProductMeasurment(measurementName="Hips", minValue=87.0, maxValue=90.0),
            ProductMeasurment(measurementName="Waist", minValue=70.0, maxValue=76.0),
        ]
    ),

    SizeConstraint(
        sizeName="38",
        sizeOrder=2,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=164.0, maxValue=175.0),
            ProductMeasurment(measurementName="Hips", minValue=91.0, maxValue=94.0),
            ProductMeasurment(measurementName="Waist", minValue=74.0, maxValue=80.0),
        ]
    ),

    SizeConstraint(
        sizeName="40",
        sizeOrder=3,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=164.0, maxValue=175.0),
            ProductMeasurment(measurementName="Hips", minValue=95.0, maxValue=98.0),
            ProductMeasurment(measurementName="Waist", minValue=78.0, maxValue=84.0),
        ]
    ),

    SizeConstraint(
        sizeName="42",
        sizeOrder=4,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=174.0, maxValue=182.0),
            ProductMeasurment(measurementName="Hips", minValue=99.0, maxValue=102.0),
            ProductMeasurment(measurementName="Waist", minValue=82.0, maxValue=88.0),
        ]
    ),

    SizeConstraint(
        sizeName="44",
        sizeOrder=5,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=174.0, maxValue=182.0),
            ProductMeasurment(measurementName="Hips", minValue=103.0, maxValue=106.0),
            ProductMeasurment(measurementName="Waist", minValue=86.0, maxValue=92.0),
        ]
    ),

    SizeConstraint(
        sizeName="46",
        sizeOrder=6,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=180.0, maxValue=188.0),
            ProductMeasurment(measurementName="Hips", minValue=107.0, maxValue=110.0),
            ProductMeasurment(measurementName="Waist", minValue=90.0, maxValue=96.0),
        ]
    ),

    SizeConstraint(
        sizeName="48",
        sizeOrder=7,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=180.0, maxValue=188.0),
            ProductMeasurment(measurementName="Hips", minValue=111.0, maxValue=114.0),
            ProductMeasurment(measurementName="Waist", minValue=94.0, maxValue=100.0),
        ]
    ),

    SizeConstraint(
        sizeName="50",
        sizeOrder=8,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=187.0, maxValue=194.0),
            ProductMeasurment(measurementName="Hips", minValue=115.0, maxValue=118.0),
            ProductMeasurment(measurementName="Waist", minValue=98.0, maxValue=105.0),
        ]
    ),

    SizeConstraint(
        sizeName="52",
        sizeOrder=9,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=187.0, maxValue=194.0),
            ProductMeasurment(measurementName="Hips", minValue=119.0, maxValue=122.0),
            ProductMeasurment(measurementName="Waist", minValue=103.0, maxValue=110.0),
        ]
    ),

    SizeConstraint(
        sizeName="54",
        sizeOrder=10,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=192.0, maxValue=196.0),
            ProductMeasurment(measurementName="Hips", minValue=123.0, maxValue=126.0),
            ProductMeasurment(measurementName="Waist", minValue=108.0, maxValue=115.0),
        ]
    ),

    SizeConstraint(
        sizeName="56",
        sizeOrder=11,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=192.0, maxValue=196.0),
            ProductMeasurment(measurementName="Hips", minValue=127.0, maxValue=130.0),
            ProductMeasurment(measurementName="Waist", minValue=113.0, maxValue=121.0),
        ]
    ),

    SizeConstraint(
        sizeName="60",
        sizeOrder=13,
        measurements=[
            ProductMeasurment(measurementName="height", minValue=194.0, maxValue=198.0),
            ProductMeasurment(measurementName="Hips", minValue=135.0, maxValue=138.0),
            ProductMeasurment(measurementName="Waist", minValue=125.0, maxValue=133.0),
        ]
    ),
]

## mock
    # return  [
    #     SizeConstraint(
    #         sizeName="Small",
    #         sizeOrder=1,
    #         measurements=[
    #             ProductMeasurment(measurementName="Chest", minValue=88,maxValue= 94),
    #             ProductMeasurment(measurementName="Waist", minValue=75, maxValue=80)
    #         ]
    #     ),
    #     SizeConstraint(
    #         sizeName="Medium",
    #         sizeOrder=2,
    #         measurements=[
    #             ProductMeasurment(measurementName="Chest",minValue=95, maxValue=100),
    #             ProductMeasurment(measurementName="Waist", minValue=81, maxValue=85)
    #         ]
    #     ),
    #     SizeConstraint(
    #         sizeName="Large",
    #         sizeOrder=3,
    #         measurements=[
    #             ProductMeasurment(measurementName="Chest", minValue=101,maxValue= 110),
    #             ProductMeasurment(measurementName="Waist", minValue=86, maxValue=95)
    #         ]
    #     )
    # ]