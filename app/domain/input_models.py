'''
Define o modelo de dados para a entrada da API usando BaseModel do Pydantic.

'''

from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
