import random
import string
from modelo.Time import Time
from modelo.Jogador import Jogador
from visão.TelaLogin import TelaLogin
from visão.TelaAdministrador import TelaAdministrador
import tkinter as tk

class Programa:
    def __init__(self):
        # Criação dos times fixos com jogadores específicos
        self.times = self.criar_times()

    def criar_times(self):
        # Lista para armazenar os times
        times = []

        # Definindo os times e seus jogadores
        times_info = [
            {"nome": "Atlético Mineiro", "jogadores": [
                ("Carlos Silva", "Zagueiro"), ("Gustavo Oliveira", "Atacante"), 
                ("Lucas Pereira", "Meio-campista"), ("Rafael Santos", "Goleiro"), 
                ("Felipe Costa", "Lateral"), ("Eduardo Lima", "Meio-campista"), 
                ("João Carlos", "Zagueiro"), ("Marcelo Rocha", "Atacante"),
                ("Thiago Almeida", "Meio-campista"), ("José Martins", "Atacante"),
                ("Ricardo Souza", "Zagueiro")
            ]},
            {"nome": "Cruzeiro", "jogadores": [
                ("Lucas Pereira", "Meio-campista"), ("Rafael Santos", "Goleiro"),
                ("Felipe Costa", "Zagueiro"), ("Eduardo Lima", "Atacante"), 
                ("Marcelo Rocha", "Meio-campista"), ("Gabriel Souza", "Lateral"), 
                ("Thiago Almeida", "Zagueiro"), ("José Martins", "Meio-campista"),
                ("Carlos Silva", "Atacante"), ("Gustavo Oliveira", "Zagueiro"),
                ("Ricardo Souza", "Atacante")
            ]},
            {"nome": "Flamengo", "jogadores": [
                ("Thiago Almeida", "Atacante"), ("Gabriel Souza", "Lateral"), 
                ("Ricardo Souza", "Meio-campista"), ("Carlos Silva", "Zagueiro"), 
                ("Lucas Pereira", "Goleiro"), ("Felipe Costa", "Atacante"), 
                ("Rafael Santos", "Meio-campista"), ("Eduardo Lima", "Zagueiro"),
                ("Marcelo Rocha", "Atacante"), ("José Martins", "Lateral"), 
                ("Gustavo Oliveira", "Meio-campista")
            ]},
            {"nome": "Corinthians", "jogadores": [
                ("Felipe Costa", "Zagueiro"), ("Eduardo Lima", "Meio-campista"), 
                ("Gabriel Souza", "Lateral"), ("Ricardo Souza", "Goleiro"), 
                ("Thiago Almeida", "Atacante"), ("Carlos Silva", "Zagueiro"),
                ("Rafael Santos", "Meio-campista"), ("Marcelo Rocha", "Atacante"),
                ("José Martins", "Meio-campista"), ("Lucas Pereira", "Zagueiro"),
                ("Gustavo Oliveira", "Atacante")
            ]},
            {"nome": "Botafogo", "jogadores": [
                ("André Rocha", "Goleiro"), ("José Martins", "Atacante"),
                ("Carlos Silva", "Zagueiro"), ("Ricardo Souza", "Meio-campista"),
                ("Marcelo Rocha", "Meio-campista"), ("Thiago Almeida", "Lateral"),
                ("Felipe Costa", "Zagueiro"), ("Eduardo Lima", "Atacante"),
                ("Lucas Pereira", "Meio-campista"), ("Gustavo Oliveira", "Zagueiro"),
                ("Rafael Santos", "Meio-campista")
            ]}
        ]

        for time_info in times_info:
            time = Time(time_info["nome"], "Técnico " + time_info["nome"])
            for jogador_nome, jogador_posicao in time_info["jogadores"]:
                jogador = Jogador(jogador_nome, random.randint(1, 99), jogador_posicao)
                time.addJogador(jogador)
            times.append(time)

        return times

    def iniciar(self):
        # Cria a janela de login e passa a lista de times
        root = tk.Tk()
        tela_login = TelaLogin(root, self.times)
        root.mainloop()

# Para rodar o programa
if __name__ == "__main__":
    programa = Programa()
    programa.iniciar()
