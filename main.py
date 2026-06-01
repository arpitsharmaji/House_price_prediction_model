from fastapi import FastAPI, Request
from app.model_loader import model
from app.inference import predict
from app.schemas import InputData
from app.database.db import Base, engine
from app.database.models_db import Prediction
from app.router import task_routes
from app.user.router import user_routes

# from models import preprocessing
# from models.preprocessing import FeatureEngineer, preprocessor 

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(task_routes)
app.include_router(user_routes)



@app.post("/predict")

def get_prediction(data: InputData):

    result = predict(data, model)

    return {"prediction": result.tolist()}
    
    
    