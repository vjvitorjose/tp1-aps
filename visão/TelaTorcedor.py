import tkinter as tk
from tkinter import messagebox
from modelo.Time import Time
from modelo.Jogador import Jogador

class TelaTorcedor:


    def __init__(self, window, times_cadastrados):
        self.window = window
        self.times_cadastrados = times_cadastrados
        
        self.window.title("Tela Torcedor")
        self.window.geometry("400x400")
        
        self.btn_visualizar_times = tk.Button(self.window, text="Visualizar Times", command=self.visualizar_times)
        self.btn_visualizar_times.pack(padx=10, pady=10)

        self.btn_verificar_tabela = tk.Button(self.window, text="Verificar Tabela", command=self.verificar_tabela)
        self.btn_verificar_tabela.pack(padx=10, pady=10)
        
        self.btn_logout = tk.Button(self.window, text="Logout", command=self.logout)
        self.btn_logout.pack(padx=10, pady=10)

    def visualizar_times(self):
        if not self.times_cadastrados:
            messagebox.showinfo("Nenhum Time Cadastrado", "Não há times cadastrados para visualizar.")
            return

        times = "\n".join([time.nome for time in self.times_cadastrados])
        messagebox.showinfo("Times Cadastrados", f"Times cadastrados:\n{times}")

    def verificar_tabela(self):
        messagebox.showinfo("Tabela", "Verificar Tabela")
    
    def logout(self):
        self.window.destroy()
