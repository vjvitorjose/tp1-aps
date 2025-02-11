import tkinter as tk
from tkinter import messagebox

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from visão.VisaoJogador import VisaoJogador
from visão.VisaoPartida import VisaoPartida
from visão.VisaoTime import VisaoTime

class TelaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")

        # Texto de introdução
        self.label_intro = tk.Label(master, text="Escolha o tipo de usuário:", font=("Arial", 14))
        self.label_intro.grid(row=0, column=0, columnspan=2, pady=10)

        # Botão para login como Administrador
        self.botao_admin = tk.Button(master, text="Administrador", width=20, command=self.abrir_tela_admin)
        self.botao_admin.grid(row=1, column=0, padx=10, pady=10)

        # Botão para login como Torcedor
        self.botao_torcedor = tk.Button(master, text="Torcedor", width=20, command=self.abrir_tela_torcedor)
        self.botao_torcedor.grid(row=1, column=1, padx=10, pady=10)

    def abrir_tela_admin(self):
        # Fechar a tela de login e abrir a tela de administração
        self.master.destroy()  # Fechar a tela de login
        root = tk.Tk()
        app = TelaAdmin(root)
        root.mainloop()

    def abrir_tela_torcedor(self):
        # Fechar a tela de login e abrir a tela do torcedor
        self.master.destroy()  # Fechar a tela de login
        root = tk.Tk()
        app = TelaTorcedor(root)
        root.mainloop()

class TelaAdmin:
    def __init__(self, master):
        self.master = master
        self.master.title("Administração")

        # Botões de administrador para gerenciar entidades
        self.botao_jogador = tk.Button(master, text="Gerenciar Jogadores", command=self.abrir_vision_jogador)
        self.botao_jogador.grid(row=0, column=0, padx=10, pady=10)
        
        self.botao_time = tk.Button(master, text="Gerenciar Times", command=self.abrir_vision_time)
        self.botao_time.grid(row=1, column=0, padx=10, pady=10)
        
        self.botao_partida = tk.Button(master, text="Gerenciar Partidas", command=self.abrir_vision_partida)
        self.botao_partida.grid(row=2, column=0, padx=10, pady=10)

    def abrir_vision_jogador(self):
        tela = tk.Tk()  # Cria uma nova janela
        app = VisaoJogador(tela)  # Passa a janela para a classe VisaoJogador
        tela.mainloop()  # Inicia o loop de eventos da nova janela

    def abrir_vision_time(self):
        tela = tk.Tk()  # Cria uma nova janela
        app = VisaoTime(tela)  # Passa a janela para a classe VisaoTime
        tela.mainloop()  # Inicia o loop de eventos da nova janela

    def abrir_vision_partida(self):
        tela = tk.Tk()  # Cria uma nova janela
        app = VisaoPartida(tela)  # Passa a janela para a classe VisaoPartida
        tela.mainloop()  # Inicia o loop de eventos da nova janela

class TelaTorcedor:
    def __init__(self, master):
        self.master = master
        self.master.title("Torcedor")

        # Botões de torcedor, apenas para carregar as informações
        self.botao_carregar_jogadores = tk.Button(master, text="Carregar Jogadores", command=self.carregar_jogadores)
        self.botao_carregar_jogadores.grid(row=0, column=0, padx=10, pady=10)
        
        self.botao_carregar_times = tk.Button(master, text="Carregar Times", command=self.carregar_times)
        self.botao_carregar_times.grid(row=1, column=0, padx=10, pady=10)
        
        self.botao_carregar_partidas = tk.Button(master, text="Carregar Partidas", command=self.carregar_partidas)
        self.botao_carregar_partidas.grid(row=2, column=0, padx=10, pady=10)

    def carregar_jogadores(self):
        tela = tk.Tk()  # Cria uma nova janela
        app = VisaoJogador(tela)  # Passa a janela para a classe VisaoJogador
        tela.mainloop()  # Inicia o loop de eventos da nova janela

    def carregar_times(self):
        tela = tk.Tk()  # Cria uma nova janela
        app = VisaoTime(tela)  # Passa a janela para a classe VisaoTime
        tela.mainloop()  # Inicia o loop de eventos da nova janela

    def carregar_partidas(self):
        tela = tk.Tk()  # Cria uma nova janela
        app = VisaoPartida(tela)  # Passa a janela para a classe VisaoPartida
        tela.mainloop()  # Inicia o loop de eventos da nova janela

# Main para iniciar a tela de login
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()
