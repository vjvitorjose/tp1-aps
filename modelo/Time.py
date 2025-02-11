from modelo.Jogador import Jogador

class Time:
    def __init__(self, nome, jogadores=None, pontuacao=0):
        self.nome = nome
        self.jogadores = jogadores if jogadores else []
        self.pontuacao = pontuacao
    
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
    
    def __str__(self):
        return f"Time: {self.nome}, Pontuação: {self.pontuacao}"
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "jogadores": [j.to_dict() for j in self.jogadores],
            "pontuacao": self.pontuacao
        }
    
    @staticmethod
    def from_dict(data):
        jogadores = [Jogador.from_dict(j) for j in data["jogadores"]]
        return Time(data["nome"], jogadores, data["pontuacao"])