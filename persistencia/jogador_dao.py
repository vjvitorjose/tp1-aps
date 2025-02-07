import json
from modelo.Jogador import Jogador

class JogadorDAO:
    _instance = None

    @staticmethod
    def get_instance():
        if JogadorDAO._instance is None:
            JogadorDAO._instance = JogadorDAO()
        return JogadorDAO._instance

    def __init__(self):
        if JogadorDAO._instance is not None:
            raise Exception("Singleton instance already created.")
        
        self.file_name = 'jogadores.json'

    def save(self, jogadores):
        jogadores_data = []
        for jogador in jogadores:
            jogadores_data.append({
                'nome': jogador.nome,
                'posicao': jogador.posicao
            })

        with open(self.file_name, 'w') as arquivo:
            json.dump(jogadores_data, arquivo, indent=4)

    def load(self):
        try:
            with open(self.file_name, 'r') as arquivo:
                jogadores_data = json.load(arquivo)
            return [Jogador(jogador['nome'], jogador['idade'], jogador['posicao']) for jogador in jogadores_data]
        except FileNotFoundError:
            return []
