import json
from modelo.Partida import Partida

class ControlePartida:
    @staticmethod
    def salvar_partidas(partidas, arquivo="partidas.json"):
        with open(arquivo, "w") as f:
            json.dump([p.to_dict() for p in partidas], f, indent=4)
    
    @staticmethod
    def carregar_partidas(arquivo="partidas.json"):
        try:
            with open(arquivo, "r") as f:
                data = json.load(f)
            return [Partida.from_dict(p) for p in data]
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou estiver vazio, retorna uma lista vazia
            return []
