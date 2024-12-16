class Partida:
    def __init__(self, equipe1, equipe2, placar1, placar2, data_jogo):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.placar1 = placar1
        self.placar2 = placar2
        self.data_jogo = data_jogo
        self.resultado_jogo = self.calcula_resultado_jogo()

    def calcula_resultado_jogo(self):
        """Calcula o resultado do jogo"""
        if self.placar1 > self.placar2:
            return f"{self.equipe1} venceu o jogo."
        elif self.placar2 > self.placar1:
            return f"{self.equipe2} venceu o jogo."
        else:
            return "O jogo terminou empatado."
            
    def __str__(self):
        return f"{self.equipe1} {self.placar1} x {self.placar2} {self.equipe2} - Data: {self.data_jogo}\nResultado: {self.resultado_jogo}"
