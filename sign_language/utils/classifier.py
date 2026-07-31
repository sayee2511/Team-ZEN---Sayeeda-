import pickle
import pandas as pd


class SignClassifier:
    def __init__(self, model_path="sign_language/models/sign_model.pkl"):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        # Feature names used during training
        self.columns = []
        for i in range(21):
            self.columns.extend([f"x{i}", f"y{i}", f"z{i}"])

    def predict(self, landmarks):
        """
        Predict sign from 63 landmarks.

        Returns:
            prediction
            confidence
        """

        if len(landmarks) != 63:
            return None, 0

        sample = pd.DataFrame([landmarks], columns=self.columns)

        prediction = self.model.predict(sample)[0]

        confidence = max(self.model.predict_proba(sample)[0]) * 100

        return prediction, confidence