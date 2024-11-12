import sys
import os

# Adicionando o diretório principal ao caminho de importação
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import messagebox

class TelaTorcedor:
    def __init__(self, master, times, abrir_tela_login):
        self.master = master
        self.master.title("Painel do Torcedor")
        self.master.geometry("400x300")
        self.times = times
        self.abrir_tela_login = abrir_tela_login

        self.label_titulo = tk.Label(self.master, text="Painel do Torcedor", font=("Arial", 16))
        self.label_titulo.pack(pady=20)

        self.botao_visualizar = tk.Button(self.master, text="Visualizar Time", command=self.visualizar_time)
        self.botao_visualizar.pack(pady=10)

        self.botao_verificar_tabela = tk.Button(self.master, text="Verificar Tabela", command=self.verificar_tabela)
        self.botao_verificar_tabela.pack(pady=10)

        # Botão de logout
        self.botao_logout = tk.Button(self.master, text="Logout", command=self.logout)
        self.botao_logout.pack(pady=10)

    def visualizar_time(self):
        messagebox.showinfo("Visualizar Time", "Função para visualizar time ainda não implementada!")

    def verificar_tabela(self):
        messagebox.showinfo("Verificar Tabela", "Função para verificar tabela ainda não implementada!")

    def logout(self):
        self.master.destroy()
        self.abrir_tela_login()
