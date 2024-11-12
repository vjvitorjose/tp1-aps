class Jogador:
    
    def __init__(self, nome, numero, posicao):
        self.__nome = nome    #atributo privado
        self.__numero = numero   #atributo privado
        self.__posicao = posicao  #atributo privado
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao