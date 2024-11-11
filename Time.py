from Jogador import Jogador

class Time:
    
    def __init__(self, nome, tecnico, casa):
        self.__nome = nome
        self.__jogadores = []
        self.__tecnico = tecnico
        self.__casa = casa
        
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
        
    def getJogadores(self):
        return self.__jogadores
    
    def addJogador(self, jogador):
        self.__jogadores.append(jogador)
        
    def removeJogador(self, jogador):
        self.__jogadores.remove(jogador)
        
    def getTecnico(self):
        return self.__tecnico
    
    def setTecnico(self, tecnico):
        self.__tecnico = tecnico
        
    def getCasa(self):
        return self.__casa
    
    def setCasa(self, casa):
        self.__casa = casa