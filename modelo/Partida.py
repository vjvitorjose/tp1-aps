from modelo.Time import Time

class Partida:
    def __init__(self, time_casa, time_visitante, gols_casa=0, gols_visitante=0):
        self.time_casa = time_casa
        self.time_visitante = time_visitante
        self.gols_casa = gols_casa
        self.gols_visitante = gols_visitante
    
    def definir_placar(self, gols_casa, gols_visitante):
        self.gols_casa = gols_casa
        self.gols_visitante = gols_visitante
        if gols_casa > gols_visitante:
            self.time_casa.pontuacao += 3
        elif gols_casa < gols_visitante:
            self.time_visitante.pontuacao += 3
        else:
            self.time_casa.pontuacao += 1
            self.time_visitante.pontuacao += 1
    
    def __str__(self):
        return f"{self.time_casa.nome} {self.gols_casa} x {self.gols_visitante} {self.time_visitante.nome}"
    
    def to_dict(self):
        return {
            "time_casa": self.time_casa.to_dict(),
            "time_visitante": self.time_visitante.to_dict(),
            "gols_casa": self.gols_casa,
            "gols_visitante": self.gols_visitante
        }
    
    @staticmethod
    def from_dict(data):
        time_casa = Time.from_dict(data["time_casa"])
        time_visitante = Time.from_dict(data["time_visitante"])
        return Partida(time_casa, time_visitante, data["gols_casa"], data["gols_visitante"])