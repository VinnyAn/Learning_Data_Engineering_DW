import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.loader import load_config
from src.utils.salvar_csv import salvar_csv
from src.modules.clientes import Clientes
from src.modules.produtos import Produtos
from src.modules.vendas import Vendas

if __name__ == "__main__":
    config = load_config()

    cliente = Clientes(config)
    produto = Produtos(config)
    venda = Vendas(config)
    df_cliente = cliente.gerar_df()
    df_produto = produto.gerar_df()
    df_venda = venda.gerar_df()

    path_destino = os.path.join(os.path.dirname(__file__), '../data')

    arquivo_cliente = config['clientes']['name']
    arquivo_produto = config['produtos']['name']
    arquivo_venda = config['vendas']['name']

    salvar_csv(df_cliente, path_destino, arquivo_cliente)
    salvar_csv(df_produto, path_destino, arquivo_produto)
    salvar_csv(df_venda, path_destino, arquivo_venda)  
