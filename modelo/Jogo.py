class Jogo:

    def __int__(self, time1, time2, placar1, placar2, data_jogo):
        self.time1 = time1
        self.time2 =time2
        self.placar1 = placar1
        self.placar2 = placar2
        self.data_jogo = data_jogo
        self.resultado_jogo = self.calcula_resultado_jogo()


        def calcula_resultado_jogo(self):
            """Resultado Jogo"""
            if(self.placar1>placar2):
                return f"{self.time1} venceu o jogo."
            elif (self.placar2>placar1):
                return f"{self.time2} venceu o jogo."
            else:
                return "O jogo terminou empatado."
            
        def __str__(self):
            
          return f"{self.time1} {self.placar1} x {self.placar2} {self.time2} - Data: {self.data}"

        


