import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Paths
DATA_PATH = "sign_language/data/landmarks.csv"
MODEL_DIR = "sign_language/models"
MODEL_PATH = os.path.join(MODEL_DIR, "sign_model.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH, low_memory=False)
df["label"] = df["label"].astype(str)

# Features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

print("Training model...")
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Save model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"Model saved to: {MODEL_PATH}")