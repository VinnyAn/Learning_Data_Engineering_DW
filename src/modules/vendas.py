import pandas as pd
import random
from faker import Faker
from utils.loader import load_config

class Vendas:
    def __init__(self, config):
        self.config = config
        self.n_clientes = self.config['clientes']['n']
        self.n_lista_produtos = self.config['produtos']['lista']
        self.n_vendas = self.config['vendas']['n']
        

    def gerar_df(self):
        dados_vendas = [
        {
            "id" : i + 1,
            "id_cliente": random.randint(1, self.n_clientes),
            "id_produto": random.randint(1, len(self.n_lista_produtos)),
            "quantidade": random.randint(1, 5),
            "valor": round(random.uniform(10, 100), 2),
        }
        for i in range(self.n_vendas)
        ]

        Vendas_df = pd.DataFrame(dados_vendas)
        return Vendas_df



