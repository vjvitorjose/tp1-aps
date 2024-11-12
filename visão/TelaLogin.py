import tkinter as tk
from tkinter import messagebox
from visão.TelaAdministrador import TelaAdministrador
from visão.TelaTecnico import TelaTecnico
from visão.TelaTorcedor import TelaTorcedor
from visão.TelaSelecaoTime import TelaSelecaoTime

class TelaLogin:
    def __init__(self, master, times):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("300x250")
        self.times = times

        self.label_nome = tk.Label(self.master, text="Digite seu nome:")
        self.label_nome.pack(pady=10)
        
        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.pack(pady=5)
        
        var = tk.StringVar()
        
        self.botao_administrador = tk.Radiobutton(self.master, text="Administrador", variable=var, value="Administrador")
        self.botao_administrador.pack()

        self.botao_tecnico = tk.Radiobutton(self.master, text="Técnico", variable=var, value="Técnico")
        self.botao_tecnico.pack()

        self.botao_torcedor = tk.Radiobutton(self.master, text="Torcedor", variable=var, value="Torcedor")
        self.botao_torcedor.pack()

        self.botao_login = tk.Button(self.master, text="Login", command=lambda: self.login(var.get()))
        self.botao_login.pack(pady=20)

    def abrir_tela_login(self):
        root = tk.Tk()
        TelaLogin(root, self.times)  # Chama a tela de login, passando os times
        root.mainloop()


    # Na TelaLogin
def login(self, tipo_usuario):
    if tipo_usuario == "Administrador":
        self.master.destroy()
        root_admin = tk.Tk()
        TelaAdministrador(root_admin, self.times, self.abrir_tela_login)
        root_admin.mainloop()
    elif tipo_usuario == "Técnico":
        self.master.destroy()
        root_selecao = tk.Tk()
        # Passa o time selecionado para abrir a tela do Técnico
        TelaSelecaoTime(root_selecao, self.times, lambda time_selecionado: self.abrir_tela_tecnico(time_selecionado))
        root_selecao.mainloop()
    elif tipo_usuario == "Torcedor":
        self.master.destroy()
        root_torcedor = tk.Tk()
        TelaTorcedor(root_torcedor, self.times, self.abrir_tela_login)
        root_torcedor.mainloop()

# Função que vai abrir a tela do técnico
def abrir_tela_tecnico(self, time_selecionado):
    root_tecnico = tk.Tk()
    # Passa o time selecionado para a TelaTecnico
    TelaTecnico(root_tecnico, self.times, self.abrir_tela_login, time_selecionado)
    root_tecnico.mainloop()
