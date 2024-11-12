import sys
import os

# Adicionando o diretório principal ao caminho de importação
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import messagebox

class TelaAdministrador:
    def __init__(self, master, times, abrir_tela_login):
        self.master = master
        self.master.title("Tela de Administrador")
        self.master.geometry("400x300")
        self.times = times
        self.abrir_tela_login = abrir_tela_login  # Função para abrir a tela de login

        self.label_titulo = tk.Label(self.master, text="Área do Administrador", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.botao_cadastrar = tk.Button(self.master, text="Cadastrar Time", command=self.cadastrar_time)
        self.botao_cadastrar.pack(pady=10)

        self.botao_atualizar = tk.Button(self.master, text="Atualizar Time", command=self.atualizar_time)
        self.botao_atualizar.pack(pady=10)

        self.botao_remover = tk.Button(self.master, text="Remover Time", command=self.remover_time)
        self.botao_remover.pack(pady=10)

        self.botao_visualizar = tk.Button(self.master, text="Visualizar Time", command=self.visualizar_time)
        self.botao_visualizar.pack(pady=10)

        self.botao_adicionar_jogo = tk.Button(self.master, text="Adicionar Jogo", command=self.adicionar_jogo)
        self.botao_adicionar_jogo.pack(pady=10)

        self.botao_verificar_tabela = tk.Button(self.master, text="Verificar Tabela", command=self.verificar_tabela)
        self.botao_verificar_tabela.pack(pady=10)

        # Botão de logout
        self.botao_logout = tk.Button(self.master, text="Logout", command=self.logout)
        self.botao_logout.pack(pady=10)

    def cadastrar_time(self):
        messagebox.showinfo("Cadastrar Time", "Função para cadastrar time ainda não implementada!")

    def atualizar_time(self):
        messagebox.showinfo("Atualizar Time", "Função para atualizar time ainda não implementada!")

    def remover_time(self):
        messagebox.showinfo("Remover Time", "Função para remover time ainda não implementada!")

    def visualizar_time(self):
        messagebox.showinfo("Visualizar Time", "Função para visualizar time ainda não implementada!")

    def adicionar_jogo(self):
        messagebox.showinfo("Adicionar Jogo", "Função para adicionar jogo ainda não implementada!")

    def verificar_tabela(self):
        messagebox.showinfo("Verificar Tabela", "Função para verificar tabela ainda não implementada!")

    def logout(self):
        self.master.destroy()  # Fecha a tela de administrador
        self.abrir_tela_login()  # Retorna para a tela de login
