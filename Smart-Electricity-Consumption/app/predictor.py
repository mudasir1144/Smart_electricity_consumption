import os
import joblib


class ElectricityPredictor:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.model = joblib.load(
            os.path.join(base_dir, "models", "best_model.pkl")
        )

        self.scaler = joblib.load(
            os.path.join(base_dir, "models", "scaler.pkl")
        )

        self.encoder = joblib.load(
            os.path.join(base_dir, "models", "encoder.pkl")
        )

    def preprocess(self, input_data):

        data = input_data.copy()

        categorical_columns = [
            "House_Type",
            "Season",
            "Day_Type",
            "Work_From_Home",
            "Solar_Panels"
        ]

        for column in categorical_columns:
            data[column] = self.encoder[column].transform(data[column])

        return self.scaler.transform(data)

    def predict(self, input_data):

        processed = self.preprocess(input_data)

        prediction = self.model.predict(processed)

        return round(float(prediction[0]), 2)