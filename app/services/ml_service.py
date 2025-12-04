import joblib
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent  # points to "app" directory

def predict(mesurment  , input):
    print('predincting for mesurment ' , mesurment,"and input" , input)
    if(input.gender=="male" and mesurment=="Underchest"):
        return float(-1)
    model_path = BASE_DIR / "models" / input.gender / f"best_model_{mesurment}.pkl"
    model=joblib.load(model_path)
    if input.gender== "female":
        return float(model.predict(pd.DataFrame([{
            "age": input.age,
            "gender": input.gender,
            "weight": input.weight,
            "height": input.height,
            "body_shape": input.body_shape,
            "braRegion":input.bra.region,
            "braBand":input.bra.band,
            "braCup":input.bra.cup,

        }])))
    return float(model.predict( pd.DataFrame([{
        "age": input.age,
        "gender": input.gender,
        "weight": input.weight,
        "height": input.height,
        "body_shape": input.body_shape,
    }])))
