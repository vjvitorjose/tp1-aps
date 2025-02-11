import json
from modelo.Time import Time
from persistencia.PersistenciaTime import PersistenciaTime

def log_operacao(func):
    def wrapper(*args, **kwargs):
        print(f"Executando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class ControleTime:
    @staticmethod
    @log_operacao
    def salvar_times(times, arquivo="times.json"):
        PersistenciaTime.salvar_times(times)
    
    @staticmethod
    @log_operacao
    def carregar_times(arquivo="times.json"):
        return PersistenciaTime.carregar_times()