import pandas as pd
import random
from faker import Faker
from utils.loader import load_config

class Clientes:
    def __init__(self, config):
        self.config = config
        self.n = self.config['clientes']['n']

    def gerar_df(self):
        fake = Faker()
        dados_clientes = [
            {
                "id": i + 1,
                "nome": fake.name(),
                "email": fake.email(),
                "idade": random.randint(18, 70),
                "cidade": fake.city(),
                "data_registro": fake.date_between(start_date="-2y", end_date="-0d") ## Pegando 2 anos atras a partir de data final ("Ontem")

            }
            for i in range(self.n)
        ]

        Clientes_df = pd.DataFrame(dados_clientes)
        return Clientes_df
