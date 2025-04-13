import pandas as pd
from faker import Faker
from utils.loader import load_config

class Produtos:
    def __init__(self, config):
        self.config = config
        self.lista = self.config['produtos']['lista']

    # Gerar dados alatórios de Produtos
    def gerar_df(self):
        dados_produtos = [
        {
            "id": i + 1,
            "nome": self.lista[i]
        }
        for i in range(len(self.lista))
        ]

        Produtos_df = pd.DataFrame(dados_produtos)
        return Produtos_df
