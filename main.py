# main.py

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Create a simple pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression())
])

def train(X_train, y_train):
    pipeline.fit(X_train, y_train)
    return pipeline

def predict(X)
    return pipeline.predict(X)

