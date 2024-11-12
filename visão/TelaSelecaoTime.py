import tkinter as tk
from tkinter import messagebox
from visão.TelaTecnico import TelaTecnico   

class TelaSelecaoTime:
    def __init__(self, master, times, callback):
        self.master = master
        self.times = times
        self.callback = callback

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Selecione o time que você é técnico", font=("Arial", 14))
        self.label.pack(pady=10)

        self.lista_times = tk.Listbox(self.frame)
        for time in self.times:
            self.lista_times.insert(tk.END, time.nome)
        self.lista_times.pack(pady=20)

        self.botao_selecionar = tk.Button(self.frame, text="Selecionar", command=self.selecionar_time)
        self.botao_selecionar.pack()

    def selecionar_time(self):
        selecionado = self.lista_times.curselection()
        if selecionado:
            time_selecionado = self.times[selecionado[0]]
            # Chama a função de callback sem passar parâmetros extras
            self.callback(time_selecionado)
            self.master.destroy()
