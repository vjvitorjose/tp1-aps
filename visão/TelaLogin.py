from visão.TelaAdministrador import TelaAdministrador
from visão.TelaTorcedor import TelaTorcedor
import tkinter as tk
from tkinter import messagebox


class TelaLogin:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tela de Login")
        
        self.times_cadastrados = []  # List of teams to pass to TelaTorcedor
        self.create_widgets()

    def create_widgets(self):
        self.label_nome = tk.Label(self.window, text="Digite seu nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=5)
        
        self.entry_nome = tk.Entry(self.window)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        self.label_tipo_usuario = tk.Label(self.window, text="Selecione o tipo de usuário:")
        self.label_tipo_usuario.grid(row=1, column=0, padx=10, pady=5)

        self.tipo_usuario_var = tk.StringVar()
        self.tipo_usuario_var.set("torcedor")
        
        self.radio_admin = tk.Radiobutton(
            self.window, text="Administrador", variable=self.tipo_usuario_var, value="administrador"
        )
        self.radio_admin.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.radio_torcedor = tk.Radiobutton(
            self.window, text="Torcedor", variable=self.tipo_usuario_var, value="torcedor"
        )
        self.radio_torcedor.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.btn_login = tk.Button(self.window, text="Entrar", command=self.login)
        self.btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        nome = self.entry_nome.get()
        tipo_usuario = self.tipo_usuario_var.get()

        if not nome.strip():
            messagebox.showwarning("Aviso", "Por favor, digite seu nome.")
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.focus()
            return

        self.window.quit()
        self.window.destroy()

        if tipo_usuario == "administrador":
            tela_admin = TelaAdministrador()
            tela_admin.run()
        elif tipo_usuario == "torcedor":
            new_window = tk.Tk()  # Create a new window for TelaTorcedor
            tela_torcedor = TelaTorcedor(new_window, self.times_cadastrados)  # Pass arguments
            new_window.mainloop()
        else:
            messagebox.showinfo("Erro", "Tipo de usuário inválido.")

    def run(self):
        self.window.mainloop()
