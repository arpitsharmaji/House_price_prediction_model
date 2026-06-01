from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.model_selection import train_test_split
from models.preprocessing import FeatureEngineer, preprocessor
from training_data_loader import load_data

pipeline = Pipeline([
    ("feature_engineering", FeatureEngineer()),
    ("preprocessing", preprocessor),
    ("model", LinearRegression())
])

# load data
path = 'models/dataset/house_data.csv'
df = load_data(path)

# split features and target
X = df.drop("price", axis=1)
y = df["price"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
pipeline.fit(X_train, y_train)

# Save it
joblib.dump(pipeline, "pipeline.pkl")