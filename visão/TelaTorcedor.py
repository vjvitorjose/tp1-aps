import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from modelo.Time import Time
from modelo.Jogador import Jogador
from visão.TelaAdministrador import TelaAdministrador

class TelaTorcedor:

    def __init__(self, window, times_cadastrados):
        self.window = window
        self.times_cadastrados = times_cadastrados
        
        self.window.title("Tela Torcedor")
        self.window.geometry("400x400")
        
        # Campo de entrada para o nome do time
        self.lbl_nome_time = tk.Label(self.window, text="Digite o seu time:")
        self.lbl_nome_time.pack(padx=10, pady=5)

        self.entry_time = tk.Entry(self.window)
        self.entry_time.pack(padx=10, pady=5)
        self.btn_visualizar_times = tk.Button(self.window, text="Visualizar Times", command=self.visualizar_times)
        self.btn_visualizar_times.pack(padx=10, pady=10)

        self.btn_verificar_tabela = tk.Button(self.window, text="Verificar Tabela", command=self.verificar_tabela)
        self.btn_verificar_tabela.pack(padx=10, pady=10)
        
        self.btn_verificar_time = tk.Button(self.window, text="Verificar Informações do Time", command=self.verificar_informacoes_time)
        self.btn_verificar_time.pack(padx=10, pady=10)
        
        self.btn_logout = tk.Button(self.window, text="Logout", command=self.logout)
        self.btn_logout.pack(padx=10, pady=10)



    def visualizar_times(self):
        if not self.times_cadastrados:
            messagebox.showinfo("Nenhum Time Cadastrado", "Não há times cadastrados para visualizar.")
            return

        times = "\n".join([time.nome for time in self.times_cadastrados])
        messagebox.showinfo("Times Cadastrados", f"Times cadastrados:\n{times}")

    def verificar_tabela(self):

        tabela_window = tk.Toplevel(self.window)
        tabela_window.title("Tabela de Times")
        tabela_window.geometry("400x400")

     
        tree = ttk.Treeview(tabela_window, columns=("Time", "Pontos"), show="headings")

       
        tree.heading("Time", text="Time")
        tree.heading("Pontos", text="Pontos")

      
        for time in self.times_cadastrados:
            tree.insert("", tk.END, values=(time.nome, time.pontos))

      
        scrollbar = tk.Scrollbar(tabela_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack(expand=True, fill="both")

        
    def verificar_informacoes_time(self):
        nome_time = self.entry_time.get().strip()
        if not nome_time:
            messagebox.showinfo("Erro", "Por favor, digite o nome de um time.")
            return

        time_selecionado = next((time for time in self.times_cadastrados if time.nome.lower() == nome_time.lower()), None)
        
        if time_selecionado:

            informacoes = (f"Nome: {time_selecionado.nome}\n"
                           f"Pontos: {time_selecionado.pontos}\n"
                           f"Gols: {time_selecionado.gols}\n"
                           f"Jogadores: {', '.join([jogador.nome for jogador in time_selecionado.jogadores])}")
            messagebox.showinfo("Informações do seu Time", informacoes)
        else:
            messagebox.showinfo("Erro", "Time não encontrado. Verifique o nome digitado.")

    def logout(self):
        self.window.destroy()
