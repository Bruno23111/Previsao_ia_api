'''
Repositório que encapsula a lógica de predição. Ele utiliza o modelo carregado para fazer as previsões.
'''

class PredictionRepository:
    def __init__(self, model):
        self.model = model

    def predict(self, text: str):
        return self.model.predict([text])[0]