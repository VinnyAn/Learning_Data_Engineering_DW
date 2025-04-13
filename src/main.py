import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.loader import load_config
from src.utils.salvar_csv import salvar_csv
from src.modules.clientes import Cliente

if __name__ == "__main__":
    config = load_config()
    cliente = Cliente(config)
    df = cliente.gerar_df()
    path_destino = os.path.join(os.path.dirname(__file__), '../data')
    nome_arquivo = "clientes.csv"
    salvar_csv(df, path_destino, nome_arquivo)