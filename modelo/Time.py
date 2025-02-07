from modelo.Jogador import Jogador
import json

class Time:
    
    def __init__(self, nome, tecnico, pontuacao=0):
        self.__nome = nome           # atributo privado
        self.__jogadores = []        # atributo privado
        self.__tecnico = tecnico     # atributo privado
        self.__pontuacao = pontuacao # atributo privado
       
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
        if pontos >= 0 and self.__pontuacao - pontos >= 0:
            self.__pontuacao -= pontos
        else:
            print("A pontuação não pode ser negativa.")

    def salvar_em_arquivo(self, nome_arquivo):
        data = {
            'Nome': self.__nome,
            'Tecnico': self.__tecnico,
            'Pontos': self.__pontuacao,
            'Jogadores': [jogador.nome for jogador in self.__jogadores]  # Corrigido para 'Jogadores'
        }
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(data, arquivo, indent=4)
        
    # Método para carregar o time a partir de um arquivo JSON
    @classmethod
    def carregar_de_arquivo(cls, nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            data = json.load(arquivo)
            
        time = cls(nome=data['Nome'], tecnico=data['Tecnico'], pontuacao=data['Pontos'])
        
        for nome_jogador in data['Jogadores']:  # Corrigido para 'Jogadores'
            jogador = Jogador(nome=nome_jogador)  # Supondo que o Jogador tenha um método de inicialização que aceita apenas o nome
            time.addJogador(jogador)
        
        return time
