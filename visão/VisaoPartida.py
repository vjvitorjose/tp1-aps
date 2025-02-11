import tkinter as tk
from tkinter import messagebox

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controle.ControlePartida import ControlePartida
from controle.ControleTime import ControleTime
from modelo.Partida import Partida
from modelo.Time import Time

class VisaoPartida:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Partidas")

        self.controle_partida = ControlePartida()
        self.controle_time = ControleTime()

        # Criando os campos de entrada para a partida
        self.label_time_casa = tk.Label(master, text="Escolha o Time da Casa:")
        self.label_time_casa.grid(row=0, column=0)
        self.lista_time_casa = tk.Listbox(master)
        self.lista_time_casa.grid(row=0, column=1)
        
        self.label_time_visitante = tk.Label(master, text="Escolha o Time Visitante:")
        self.label_time_visitante.grid(row=1, column=0)
        self.lista_time_visitante = tk.Listbox(master)
        self.lista_time_visitante.grid(row=1, column=1)

        # Carregar times nas listas de escolha
        self.carregar_times()

        # Campos para o placar
        self.label_placar = tk.Label(master, text="Placar:")
        self.label_placar.grid(row=2, column=0)
        self.entry_gols_casa = tk.Entry(master)
        self.entry_gols_casa.grid(row=2, column=1)
        self.entry_gols_visitante = tk.Entry(master)
        self.entry_gols_visitante.grid(row=2, column=2)

        # Botões
        self.botao_cadastrar_partida = tk.Button(master, text="Cadastrar Partida", command=self.cadastrar_partida)
        self.botao_cadastrar_partida.grid(row=3, column=0)

        self.botao_excluir_partida = tk.Button(master, text="Excluir Partida", command=self.excluir_partida)
        self.botao_excluir_partida.grid(row=3, column=1)

        self.botao_carregar_partidas = tk.Button(master, text="Carregar Partidas", command=self.carregar_partidas)
        self.botao_carregar_partidas.grid(row=4, column=0)

        # Lista de partidas
        self.lista_partidas = tk.Listbox(master)
        self.lista_partidas.grid(row=5, column=0, columnspan=3, sticky="nsew")

    def carregar_times(self):
        times = self.controle_time.carregar_times()
        for time in times:
            self.lista_time_casa.insert(tk.END, time.nome)
            self.lista_time_visitante.insert(tk.END, time.nome)

    def cadastrar_partida(self):
        # Obtendo os times e placar
        time_casa_nome = self.lista_time_casa.get(tk.ACTIVE)
        time_visitante_nome = self.lista_time_visitante.get(tk.ACTIVE)
        gols_casa = self.entry_gols_casa.get()
        gols_visitante = self.entry_gols_visitante.get()

        if time_casa_nome and time_visitante_nome and gols_casa.isdigit() and gols_visitante.isdigit():
            gols_casa = int(gols_casa)
            gols_visitante = int(gols_visitante)

            # Encontrando os objetos de Time
            times = self.controle_time.carregar_times()
            time_casa = next((t for t in times if t.nome == time_casa_nome), None)
            time_visitante = next((t for t in times if t.nome == time_visitante_nome), None)

            if time_casa and time_visitante:
                partida = Partida(time_casa, time_visitante, gols_casa, gols_visitante)
                partidas = self.controle_partida.carregar_partidas()
                partidas.append(partida)
                self.controle_partida.salvar_partidas(partidas)
                self.atualizar_lista()
                messagebox.showinfo("Sucesso", "Partida cadastrada com sucesso!")
        else:
            messagebox.showwarning("Campos inválidos", "Por favor, preencha corretamente os campos.")

    def excluir_partida(self):
        selecionada = self.lista_partidas.curselection()
        if selecionada:
            partida_selecionada = self.lista_partidas.get(selecionada)
            print(f"Partida selecionada: {partida_selecionada}")  # Para depuração

            # Extração dos nomes dos times (sem os gols)
            time_casa_nome = partida_selecionada.split(" x ")[0].strip()
            time_visitante_nome = partida_selecionada.split(" x ")[1].split(" ")[0].strip()

            # Carregar as partidas existentes
            partidas = self.controle_partida.carregar_partidas()

            # Imprimir as partidas carregadas para depuração
            print(f"Partidas carregadas: {[str(p) for p in partidas]}")  # Para depuração

            # Encontrar a partida correspondente
            partida_a_excluir = None
            for partida in partidas:
                # Comparar os objetos Time diretamente
                print(f"Verificando: {partida.time_casa.nome} vs {partida.time_visitante.nome}")  # Para depuração
                if partida.time_casa.nome.strip() == time_casa_nome and partida.time_visitante.nome.strip() == time_visitante_nome:
                    partida_a_excluir = partida
                    break

            if partida_a_excluir:
                # Remover a partida da lista
                partidas.remove(partida_a_excluir)
                # Salvar a lista de partidas novamente no arquivo
                self.controle_partida.salvar_partidas(partidas)
                # Atualizar a lista na interface
                self.atualizar_lista()
                messagebox.showinfo("Sucesso", f"Partida entre {time_casa_nome} e {time_visitante_nome} excluída com sucesso!")
            else:
                messagebox.showwarning("Erro", "Partida não encontrada!")
        else:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione uma partida para excluir.")



    def carregar_partidas(self):
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_partidas.delete(0, tk.END)
        partidas = self.controle_partida.carregar_partidas()
        for partida in partidas:
            self.lista_partidas.insert(tk.END, str(partida))