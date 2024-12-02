'''
Serviço que chama o repositório e manipula as exceções.
'''
from fastapi import HTTPException
from repositories.prediction_repository import PredictionRepository

class PredictionService:
    def __init__(self, prediction_repository: PredictionRepository):
        self.prediction_repository = prediction_repository

    def make_prediction(self, text: str):
        try:
            return self.prediction_repository.predict(text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))