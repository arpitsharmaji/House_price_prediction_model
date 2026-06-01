import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# -----------------------------
# Feature Engineering Class
# -----------------------------
class FeatureEngineer(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        
        # total rooms
        X['total_rooms'] = X['bedrooms'] + X['bathrooms']
        
        # age category
        X['age_category'] = pd.cut(
            X['age'],
            bins=[-1, 5, 15, 30],
            labels=[0, 1, 2]
        ).astype(int)
        
        # bed/bath ratio
        X['bed_bath_ratio'] = X['bedrooms'] / (X['bathrooms'] + 1)
        
        return X


# -----------------------------
# Columns
# -----------------------------
categorical_columns = ['location']

numerical_columns = [
    'area_sqft',
    'bedrooms',
    'bathrooms',
    'age',
    'total_rooms',
    'bed_bath_ratio',
    'age_category'
]


# -----------------------------
# Preprocessor
# -----------------------------
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_columns),
    ('num', 'passthrough', numerical_columns)
])