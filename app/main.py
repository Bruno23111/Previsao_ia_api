#pip install fastapi
#pip install unicorn
#pip intasll joblib

from fastapi import FastAPI  # Importa a classe FastAPI para criar o aplicativo web
from core.config import app  # Importa a instância do aplicativo FastAPI configurada no módulo core/config.py
from db.model_loader import ModelLoader  # Importa a classe ModelLoader para carregar o modelo de Machine Learning
from domain.input_models import TextInput  # Importa a classe TextInput, que define o modelo de entrada da API
from repositories.prediction_repository import PredictionRepository  # Importa o repositório para realizar predições
from services.prediction_service import PredictionService  # Importa o serviço de predição que encapsula a lógica
import uvicorn  # Importa o uvicorn para executar o servidor ASGI

# Inicializa e carrega o modelo de Machine Learning
# ModelLoader é uma classe responsável por carregar o modelo a partir de um arquivo
# Neste caso, o arquivo 'music_geral.robson' é carregado para o modelo de predições
model_loader = ModelLoader('models/music_geral.juliana')
model = model_loader.get_model()  # Obtém o modelo carregado para ser usado no repositório de predição

# Cria instâncias do repositório e do serviço de predição
# PredictionRepository é responsável por interagir com o modelo e realizar a predição
prediction_repository = PredictionRepository(model)
# PredictionService gerencia a lógica de negócio, chamando o repositório para realizar a predição e lidando com possíveis erros
prediction_service = PredictionService(prediction_repository)

# Define uma rota da API para a predição de música
# A anotação @app.post define um endpoint HTTP POST na rota "/api/v1/ai/music/prediction"
# A função predict recebe dados no formato TextInput (um modelo de entrada com o texto a ser classificado)
@app.post("/api/v1/ai/music/prediction")
async def predict(data: TextInput):
    # Chama o serviço de predição para processar o texto de entrada
    prediction = prediction_service.make_prediction(data.text)
    # Retorna o resultado da predição como um dicionário JSON, onde "prediction" é o valor previsto
    return {"prediction": prediction}

# Código para executar o servidor com uvicorn diretamente no script
# O servidor uvicorn é executado se o script for executado diretamente, permitindo o acesso ao app na rede
# Parâmetros: host "0.0.0.0" (acessível na rede), porta 8000, reload=True (recarga automática ao modificar o código)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)