import json
from modelo.Jogador import Jogador

class PersistenciaJogador:
    _instancia = None  # Atributo para armazenar a única instância da classe

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(PersistenciaJogador, cls).__new__(cls)
            # Inicialize aqui quaisquer atributos que você precise
        return cls._instancia

    @staticmethod
    def salvar_jogadores(jogadores, arquivo="jogadores.json"):
        with open(arquivo, "w") as f:
            json.dump([j.to_dict() for j in jogadores], f, indent=4)

    @staticmethod
    def carregar_jogadores(arquivo="jogadores.json"):
        try:
            with open(arquivo, "r") as f:
                data = json.load(f)
            return [Jogador.from_dict(j) for j in data]
        except FileNotFoundError:
            return []  # Caso o arquivo não exista ainda