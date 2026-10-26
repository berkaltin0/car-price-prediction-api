adfrom fastapi import FastAPI
from pydantic import BaseModel, Field  # Field modülünü ekledik
import pandas as pd
from autogluon.tabular import TabularPredictor

app = FastAPI(title="İkinci El Araç Fiyat Tahmin API", version="1.0")

predictor = TabularPredictor.load("autogluon_car_model")


# Doğrulama kurallarını eklediğimiz yeni veri şeması
class CarFeatures(BaseModel):
    km_driven: float = Field(..., ge=0, description="Kilometre 0'dan küçük olamaz")
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: float = Field(..., ge=0)
    engine: float = Field(..., gt=0, description="Motor hacmi 0'dan büyük olmalı")
    max_power: float = Field(..., gt=0)
    seats: float = Field(..., gt=0)
    age: float = Field(..., ge=0, description="Araç yaşı 0'dan küçük olamaz")
    brand: str
    model: str
    trim: str
    torque_nm: float = Field(..., gt=0)
    max_rpm: float = Field(..., gt=0)


@app.post("/predict")
def predict_price(car: CarFeatures):
    input_data = pd.DataFrame([car.model_dump()])
    prediction = predictor.predict(input_data)

    return {
        "status": "success",
        "predicted_selling_price": float(prediction.iloc[0])
    }


@app.get("/")
def health_check():
    return {"message": "Araç Tahmin API'si aktif olarak çalışıyor."}