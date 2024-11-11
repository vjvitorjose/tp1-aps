class Jogador:
    
    def __init__(self, nome, numero, posicao):
        self.__nome = nome
        self.__numero = numero
        self.__posicao = posicao
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, numero):
        self.__numero = numero
    
    def getPosicao(self):
        return self.__posicao
    
    def setPosicao(self, posicao):
        self.__posicao = posicao
    