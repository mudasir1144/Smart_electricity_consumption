import joblib
import pandas as pd
import os

class ElectricityPredictor:
    def __init__(self):
        Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Model_Path = os.path.join(Base_dir , 'models','best_model.pkl')
        Scaler_path = os.path.join(Base_dir , 'models' , 'scaler.pkl') 
        Encoder_path = os.path.join(Base_dir , 'models' , 'encoder.pkl')

        self.model= joblib.load(Model_Path)
        self.model = joblib.load(Scaler_path)
        self.model = joblib.load(Encoder_path)
    
    def preprocess (self , input_data):
        categorical_columns = [
            "House_Type",
            "Season",
            "Day_Type",
            "Work_From_Home",
            "Solar_Panels"
        ]

        for column in categorical_columns:
            input_data[column] = self.encoder[column].transform(input_data[column])

        scaled_data = self.scaler.tranform(input_data)
        return scaled_data
    
    def predict(self, input_data):
        processed_data = self.preprocess(input_data)
        prediction = self.model.predict(processed_data)
        return round(float(prediction[0],2))