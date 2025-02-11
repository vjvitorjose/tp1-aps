import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelo.Jogador import Jogador

import json

class ControleJogador:
    @staticmethod
    def salvar_jogadores(jogadores, arquivo="jogadores.json"):
        with open(arquivo, "w") as f:
            json.dump([j.to_dict() for j in jogadores], f, indent=4)
    
    @staticmethod
    def carregar_jogadores(arquivo="jogadores.json"):
        with open(arquivo, "r") as f:
            data = json.load(f)
        return [Jogador.from_dict(j) for j in data]