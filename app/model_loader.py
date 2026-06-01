# model_loader.py
from models import preprocessing
import sys
import os

sys.path.append(os.path.abspath("models"))
import joblib

model = joblib.load("models/pipeline.pkl")

