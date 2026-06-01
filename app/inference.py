from app.model_loader import model
import pandas as pd

def predict(data, model):
    data = data.model_dump()
    input_df = pd.DataFrame([data])
     # ✅ enforce correct feature order

    # input_df = input_df[model.feature_names_in_]
    return model.predict(input_df)