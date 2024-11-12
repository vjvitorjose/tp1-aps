class Time:
    
    def __init__(self, nome, tecnico, pontuacao=0):
        self.__nome = nome
        self.__jogadores = []
        self.__tecnico = tecnico
        self.__pontuacao = pontuacao
       
    @property 
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def jogadores(self):
        return self.__jogadores
    
    def addJogador(self, jogador):  
        if isinstance(jogador, Jogador):
            self.__jogadores.append(jogador)
        
    def removeJogador(self, jogador):
        if jogador in self.__jogadores:
            self.__jogadores.remove(jogador)
    
    @property
    def tecnico(self):
        return self.__tecnico
    
    @tecnico.setter
    def tecnico(self, tecnico):
        self.__tecnico = tecnico
        
    @property
    def pontuacao(self):
        return self.__pontuacao
    
    def addPontuacao(self, pontos):
        self.__pontuacao += pontos
        
    def removePontuacao(self, pontos):
        self.__pontuacao -= pontos