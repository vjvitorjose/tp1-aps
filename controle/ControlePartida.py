import json
from modelo.Partida import Partida
from persistencia.PersistenciaPartida import PersistenciaPartida

def log_operacao(func):
    def wrapper(*args, **kwargs):
        print(f"Executando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class ControlePartida:
    @staticmethod
    @log_operacao
    def salvar_partidas(partidas, arquivo="partidas.json"):
        PersistenciaPartida.salvar_partidas(partidas)
    
    @staticmethod
    @log_operacao
    def carregar_partidas(arquivo="partidas.json"):
        return PersistenciaPartida.carregar_partidas()
