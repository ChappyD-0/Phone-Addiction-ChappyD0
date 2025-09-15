from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import numpy as np
import pandas as pd
import pathlib, json

app = FastAPI(title='Teen Phone Addiction Prediction')
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)

MODEL_PATH = pathlib.Path('model/teen-addiction-v1.joblib')
FEATURES_PATH = pathlib.Path('model/teen-addiction-features.json')  
CSV_FALLBACK = pathlib.Path('data/teen_phone_addiction_dataset.csv')

model = load(MODEL_PATH)

def load_feature_cols():
    if FEATURES_PATH.exists():
        return json.loads(FEATURES_PATH.read_text())
    if CSV_FALLBACK.exists():
        df = pd.read_csv(CSV_FALLBACK)
        drop = [c for c in ["Name","Addiction_Level"] if c in df.columns]
        Xref = pd.get_dummies(df.drop(columns=drop), drop_first=True)
        return list(Xref.columns)
    raise RuntimeError("Faltan columnas de referencia. Guarda teen-addiction-features.json o deja el CSV en data/.")

FEATURE_COLS = load_feature_cols()

# === InputData SOLO con features (sin Name ni Addiction_Level) ===
class InputData(BaseModel):
    Age: int = 16
    Gender: str = "Male"                      # Male | Female | Other
    Location: str = "Urban"
    School_Grade: str = "10th"
    Daily_Usage_Hours: float = 5.0
    Sleep_Hours: float = 6.0
    Academic_Performance: int = 80            # 0-100
    Social_Interactions: int = 5
    Exercise_Hours: float = 1.0
    Anxiety_Level: int = 5                    # 0-10
    Depression_Level: int = 3                 # 0-10
    Self_Esteem: int = 8                      # 0-10
    Parental_Control: int = 0                 # 0/1
    Screen_Time_Before_Bed: float = 1.0
    Phone_Checks_Per_Day: int = 80
    Apps_Used_Daily: int = 10
    Time_on_Social_Media: float = 2.0
    Time_on_Gaming: float = 1.0
    Time_on_Education: float = 1.0
    Phone_Usage_Purpose: str = "Social Media" # Social Media | Gaming | Education | Browsing | Other
    Family_Communication: int = 5
    Weekend_Usage_Hours: float = 6.0

class OutputData(BaseModel):
    score: float = 0.75 

def build_features_row(p: InputData) -> pd.DataFrame:
    raw = p.dict()
    df1 = pd.DataFrame([raw])
    X = pd.get_dummies(df1, drop_first=True)
    X = X.reindex(columns=FEATURE_COLS, fill_value=0)
    return X

@app.post('/score', response_model=OutputData)
def score(data: InputData):
    try:
        X = build_features_row(data)
        proba = model.predict_proba(X)[:, -1]  
        return {'score': float(proba[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

