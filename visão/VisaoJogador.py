import tkinter as tk
from tkinter import messagebox

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.Jogador import Jogador
from controle.ControleJogador import ControleJogador

class VisaoJogador:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Jogadores")
        
        self.controle = ControleJogador()

        # Criando os campos de entrada
        self.label_nome = tk.Label(master, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.label_numero = tk.Label(master, text="Número:")
        self.label_numero.grid(row=1, column=0)
        self.entry_numero = tk.Entry(master)
        self.entry_numero.grid(row=1, column=1)

        self.label_posicao = tk.Label(master, text="Posição:")
        self.label_posicao.grid(row=2, column=0)
        self.entry_posicao = tk.Entry(master)
        self.entry_posicao.grid(row=2, column=1)

        # Botões
        self.botao_cadastrar = tk.Button(master, text="Cadastrar", command=self.cadastrar_jogador)
        self.botao_cadastrar.grid(row=3, column=0)

        self.botao_excluir = tk.Button(master, text="Excluir", command=self.excluir_jogador)
        self.botao_excluir.grid(row=3, column=1)

        self.botao_carregar = tk.Button(master, text="Carregar Jogadores", command=self.carregar_jogadores)
        self.botao_carregar.grid(row=4, column=0)

        # Lista de jogadores
        self.lista_jogadores = tk.Listbox(master)
        self.lista_jogadores.grid(row=5, column=0, columnspan=2, sticky="nsew")

    def cadastrar_jogador(self):
        nome = self.entry_nome.get()
        numero = self.entry_numero.get()
        posicao = self.entry_posicao.get()

        if nome and numero and posicao:
            jogador = Jogador(nome, int(numero), posicao)
            jogadores = self.controle.carregar_jogadores()
            jogadores.append(jogador)
            self.controle.salvar_jogadores(jogadores)
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Jogador cadastrado com sucesso!")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")

    def excluir_jogador(self):
        selecionado = self.lista_jogadores.curselection()
        if selecionado:
            jogador_selecionado = self.lista_jogadores.get(selecionado)
            nome_jogador = jogador_selecionado.split(" ")[0]
            jogadores = self.controle.carregar_jogadores()
            jogadores = [j for j in jogadores if j.nome != nome_jogador]
            self.controle.salvar_jogadores(jogadores)
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", f"Jogador {nome_jogador} excluído com sucesso!")
        else:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione um jogador para excluir.")

    def carregar_jogadores(self):
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_jogadores.delete(0, tk.END)
        jogadores = self.controle.carregar_jogadores()
        for jogador in jogadores:
            self.lista_jogadores.insert(tk.END, f"{jogador.nome} ({jogador.posicao}) - #{jogador.numero}")