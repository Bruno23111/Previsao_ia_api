
'''

Define uma classe para o carregamento do modelo.

'''
import joblib

class ModelLoader:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def get_model(self):
        return self.model