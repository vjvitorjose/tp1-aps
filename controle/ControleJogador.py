import json
from modelo.Jogador import Jogador
from persistencia.PersistenciaJogador import PersistenciaJogador

def log_operacao(func):
    def wrapper(*args, **kwargs):
        print(f"Executando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class ControleJogador:
    
    @staticmethod
    @log_operacao
    def salvar_jogadores(jogadores, arquivo="jogadores.json"):
        PersistenciaJogador.salvar_jogadores(jogadores)
    
    @staticmethod
    @log_operacao
    def carregar_jogadores(arquivo="jogadores.json"):
        return PersistenciaJogador.carregar_jogadores()