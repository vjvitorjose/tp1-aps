import tkinter as tk
from tkinter import messagebox

import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controle.ControleTime import ControleTime
from modelo.Time import Time
from modelo.Jogador import Jogador

class VisaoTime:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Times")

        self.controle = ControleTime()

        # Criando os campos de entrada
        self.label_nome_time = tk.Label(master, text="Nome do Time:")
        self.label_nome_time.grid(row=0, column=0)
        self.entry_nome_time = tk.Entry(master)
        self.entry_nome_time.grid(row=0, column=1)

        # Botões
        self.botao_cadastrar_time = tk.Button(master, text="Cadastrar Time", command=self.cadastrar_time)
        self.botao_cadastrar_time.grid(row=1, column=0)

        self.botao_excluir_time = tk.Button(master, text="Excluir Time", command=self.excluir_time)
        self.botao_excluir_time.grid(row=1, column=1)

        self.botao_carregar_times = tk.Button(master, text="Carregar Times", command=self.carregar_times)
        self.botao_carregar_times.grid(row=2, column=0)

        # Lista de times
        self.lista_times = tk.Listbox(master)
        self.lista_times.grid(row=3, column=0, columnspan=2, sticky="nsew")

    def cadastrar_time(self):
        nome_time = self.entry_nome_time.get()

        if nome_time:
            # Criando um time com o nome informado e adicionando um jogador fictício
            jogador_ficticio = Jogador("Jogador Fictício", 99, "Meio-campo")
            time = Time(nome_time)
            time.adicionar_jogador(jogador_ficticio)
            times = self.controle.carregar_times()
            times.append(time)
            self.controle.salvar_times(times)
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Time cadastrado com sucesso!")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha o nome do time.")

    def excluir_time(self):
        selecionado = self.lista_times.curselection()
        if selecionado:
            nome_time_selecionado = self.lista_times.get(selecionado).split(" -")[0]  # Extrair nome do time
            times = self.controle.carregar_times()
            times = [t for t in times if t.nome != nome_time_selecionado]  # Filtra o time a ser excluído
            self.controle.salvar_times(times)
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", f"Time {nome_time_selecionado} excluído com sucesso!")
        else:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione um time para excluir.")

    def carregar_times(self):
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_times.delete(0, tk.END)
        times = self.controle.carregar_times()
        for time in times:
            self.lista_times.insert(tk.END, f"{time.nome} - Pontuação: {time.pontuacao}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VisaoTime(root)
    root.mainloop()
