import tkinter as tk
from tkinter import messagebox

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controle.ControleJogador import ControleJogador
from modelo.Jogador import Jogador

class VisaoJogador:

    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Jogadores")
        self.jogadores = []  # Lista para armazenar os jogadores

        # Tela inicial
        self.tela_inicial()

    def tela_inicial(self):
        """Cria a tela inicial com botões para adicionar e remover jogadores."""
        self.limpar_tela()

        tk.Label(self.root, text="Gerenciador de Jogadores", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Adicionar Jogador", command=self.tela_adicionar_jogador, width=20).pack(pady=10)
        tk.Button(self.root, text="Remover Jogador", command=self.tela_remover_jogador, width=20).pack(pady=10)

    def tela_adicionar_jogador(self):
        """Cria a tela para adicionar um jogador."""
        self.limpar_tela()

        tk.Label(self.root, text="Adicionar Jogador", font=("Arial", 14)).pack(pady=10)

        # Campos de entrada
        tk.Label(self.root, text="Nome:").pack()
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)

        tk.Label(self.root, text="Número:").pack()
        self.numero_entry = tk.Entry(self.root)
        self.numero_entry.pack(pady=5)

        tk.Label(self.root, text="Posição:").pack()
        self.posicao_entry = tk.Entry(self.root)
        self.posicao_entry.pack(pady=5)

        # Botões
        tk.Button(self.root, text="Salvar", command=self.adicionar_jogador).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack(pady=5)

    def tela_remover_jogador(self):
        """Cria a tela para remover um jogador."""
        self.limpar_tela()

        tk.Label(self.root, text="Remover Jogador", font=("Arial", 14)).pack(pady=10)

        if not self.jogadores:
            tk.Label(self.root, text="Nenhum jogador cadastrado.").pack()
            tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack(pady=10)
            return

        # Lista de jogadores
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        for jogador in self.jogadores:
            self.listbox.insert(tk.END, f"{jogador['nome']} - {jogador['numero']} - {jogador['posicao']}")

        # Botão para remover
        tk.Button(self.root, text="Remover Selecionado", command=self.remover_jogador).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack(pady=5)

    @staticmethod
    def adicionar_jogador(self):
        nome = self.nome_entry.get()
        numero = self.numero_entry.get()
        posicao = self.posicao_entry.get()
        jogador = Jogador(nome, numero, posicao)
        jogadores = ControleJogador.carregar_jogadores()
        jogadores.append(jogador)
        ControleJogador.salvar_jogadores(jogadores)
        messagebox.showinfo("Sucesso", "Jogador adicionado com sucesso!")
        self.tela_inicial()
    
    @staticmethod
    def remover_jogador(nome):
        jogadores = [j for j in ControleJogador.carregar_jogadores() if j.nome != nome]
        ControleJogador.salvar_jogadores(jogadores)

    def limpar_tela(self):
        """Limpa todos os widgets da tela."""
        for widget in self.root.winfo_children():
            widget.destroy()


# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = VisaoJogador(root)
    root.mainloop()