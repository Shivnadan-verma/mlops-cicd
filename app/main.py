from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI(title="EKS + Jenkins + JFrog + FastAPI ML")

MODEL_PATH = "model.joblib"
model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ Loaded ML model from model.joblib")
else:
    print("⚠️ model.joblib not found. /predict will not work.")

class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "FastAPI ML app is running on EKS 🚀"}

@app.post("/predict")
def predict(req: IrisRequest):
    if model is None:
        return {"error": "Model not loaded. Please train and rebuild the image."}

    x = np.array([[req.sepal_length,
                   req.sepal_width,
                   req.petal_length,
                   req.petal_width]])
    pred = model.predict(x)[0]
    return {"prediction": int(pred)}
