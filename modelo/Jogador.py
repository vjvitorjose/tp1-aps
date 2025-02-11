class Jogador:
    def __init__(self, nome, numero, posicao):
        self.nome = nome
        self.numero = numero
        self.posicao = posicao
    
    def __str__(self):
        return f"{self.nome} ({self.posicao}) - #{self.numero}"

    def to_dict(self):
        return {"nome": self.nome, "numero": self.numero, "posicao": self.posicao}
    
    @staticmethod
    def from_dict(data):
        return Jogador(data["nome"], data["numero"], data["posicao"])