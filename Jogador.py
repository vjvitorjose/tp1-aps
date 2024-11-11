class Jogador:
    
    def __init__(self, nome, numero, posicao):
        self.__nome = nome
        self.__numero = numero
        self.__posicao = posicao
    
    def exibir_info(self):
        info = (
            f"Nome: {self.__nome}\n"
            f"Numero: {self.__numero}\n"
            f"Posição: {self.__posicao}\n"
        )