from tkinter import Button 
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
from .TelaCampeonato import TelaCampeonato 

class TelaUsuario:

    def __init__(self, root):

            self.root = root
            self.root.title("Fazer Login")
            self.root.geometry("600x400")

            self.bg_image = Image.open("fundo.jpg")
            self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)  
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)  

            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1) 


            self.label_nome = tk.Label(root, text="Seu Nome:", font=("Times New Roman", 20))
            self.label_nome.pack(pady=5)

            self.entry_nome = tk.Entry(root, font=("Times New Roman", 20))
            self.entry_nome.pack(pady=5)

            self.label_time = tk.Label(root, text="Time:", font=("Times New Roman", 20))
            self.label_time.pack(pady=5)

            self.entry_time = tk.Entry(root, font=("Times New Roman", 20))
            self.entry_time.pack(pady=5)


            self.label_tipo_usuario = tk.Label(root, text="Selecione Uma Opção:", font=("Times New Roman", 18))
            self.label_tipo_usuario.pack(pady=10)

            # Botões para escolher o tipo de usuário
            self.botao_torcedor = tk.Button(root, text="Torcedor", width=20, height=2, command=self.login_torcedor)
            self.botao_torcedor.pack(pady=5)

            self.botao_administrador = tk.Button(root, text="Administrador", width=20, height=2, command=self.login_administrador)
            self.botao_administrador.pack(pady=5)

            self.botao_jogador = tk.Button(root, text="Jogador", width=20, height=2, command=self.login_jogador)
            self.botao_jogador.pack(pady=5)

    def login_torcedor(self):
        nome = self.entry_nome.get()
        time = self.entry_time.get()
        if nome and time:
            self.login(nome,time, "Torcedor")
        else:
            messagebox.showwarning("Todos os campos devem ser preenchidos.")

    def login_administrador(self):
        nome = self.entry_nome.get()
        # time = self.entry_time.get()
        if nome:
            self.login(nome, "Administrador")
        else:
            messagebox.showwarning("Todos os campos devem ser preenchidos.")

    def login_jogador(self):
        nome = self.entry_nome.get()
        time = self.entry_time.get()
        if nome:
            self.login(nome,time, "Jogador")
        else:
            messagebox.showwarning("Todos os campos devem ser preenchidos.")

    def login(self, tipo_usuario, nome_usuario,time_usuario):

        self.root.destroy()  
        root_principal = tk.Tk()
        app_principal = TelaCampeonato(root_principal, tipo_usuario, nome_usuario, time_usuario)
        root_principal.mainloop()


