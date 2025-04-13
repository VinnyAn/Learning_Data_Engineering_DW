import os
from src.utils import loader

def salvar_csv(df, pasta_destino, nome_arquivo):
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
    df.to_csv(caminho_arquivo, index=False)
    print(f"Arquivo CSV salvo em: {caminho_arquivo}")