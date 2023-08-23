import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            # Load model and preprocessor
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            # Transform data
            data_transformed = preprocessor.transform(features)

            # Predict
            pred = model.predict(data_transformed)
            return pred

        except Exception as e:
            raise CustomException(e, sys)
class CustomData:
    def __init__(self,
                gender: str,
                ethnicity: str,
                parental_level_of_education: str,
                lunch: str,
                test_preparation_course: str,
                writing_score: int,
                reading_score:int):

        self.gender = gender
        self.ethnicity = ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.writing_score = writing_score
        self.reading_score = reading_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "writing_score": [self.writing_score],
                "reading_score": [self.reading_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
