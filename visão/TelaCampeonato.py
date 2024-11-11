import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TelaCampeonato:

    def __init__(self, root, usuario, nome_usuario, time_usuario):
        self.root = root
        self.root.title("Campeonato de Futebol 2024")
        self.root.geometry("600x400") 

        # Imagem de fundo
        self.bg_image = Image.open("fundo.jpg") 
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)  
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)  

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

        self.usuario = usuario  
        self.nome_usuario = nome_usuario  
        self.time_usuario = time_usuario 

        self.mensagem = tk.Label(root, text="", font=("Times New Roman", 20))
        self.mensagem.pack(pady=20)  


        self.login_usuario = tk.Label(root, text=f"Nome: {self.nome_usuario}\nTime: {self.time_usuario}", font=("Times New Roman", 20))
        self.login_usuario.pack(pady=20) 
        self.menu_frame = tk.Frame(root, bg="black") 
        self.menu_frame.pack()

        self.tipo_usuario()

    def botao(self, texto, comando):

        botao = tk.Button(self.menu_frame, text=texto, width=20, height=2, command=comando)
        botao.pack(pady=10)  

    def tipo_usuario(self):

        for widget in self.menu_frame.winfo_children():
            widget.destroy()
    
        if self.usuario == "torcedor":
            self.mensagem.config(text="ÁREA DO TORCEDOR!")
            self.botao("Classificação", self.classificacao)

        elif self.usuario == "administrador":
            self.mensagem.config(text="ÁREA DO ADMINISTRADOR!")
            self.botao("Cadastrar Time", self.cadastrar_time)
            self.botao("Gravar Resultado de uma Partida", self.gravar_resultado)

        elif self.usuario == "jogador":
            self.mensagem.config(text="ÁREA DO JOGADOR!")
            self.botao("Classificação", self.classificacao)

        for widget in self.menu_frame.winfo_children():
            widget.destroy()

    def classificacao(self):
        messagebox.showinfo("Tabela de Classificação 2024", "Aqui estará a tabela de classificação.")

    def cadastrar_time(self):
        messagebox.showinfo("Cadastrar Time", "Aqui você pode cadastrar um time.")

    def gravar_resultado(self):
        messagebox.showinfo("Gravar Resultado", "Aqui você pode gravar o resultado de uma partida.")
