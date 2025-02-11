import tkinter as tk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080")

        # Variável para armazenar o tipo de usuário
        self.tipo_usuario = tk.StringVar(value="Torcedor")

        # Variável para armazenar o nome do usuário
        self.nome_usuario = tk.StringVar()

        # Criação dos widgets
        self.label_titulo = tk.Label(root, text="Login", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(root, text="Nome:", font=16)
        self.label_nome.pack()

        self.entry_nome = tk.Entry(root, textvariable=self.nome_usuario)
        self.entry_nome.pack(pady=5)

        self.radio_torcedor = tk.Radiobutton(root, text="Torcedor", variable=self.tipo_usuario, value="Torcedor")
        self.radio_torcedor.pack()

        self.radio_admin = tk.Radiobutton(root, text="Administrador", variable=self.tipo_usuario, value="Administrador")
        self.radio_admin.pack()

        self.botao_login = tk.Button(root, text="Login", command=self.fazer_login)
        self.botao_login.pack(pady=20)

    def fazer_login(self):
        nome = self.nome_usuario.get()
        tipo = self.tipo_usuario.get()

        if nome.strip() == "":
            messagebox.showwarning("Erro", "Por favor, insira um nome.")
            return

        messagebox.showinfo("Login realizado", f"Bem-vindo, {nome}!\nVocê está logado como {tipo}.")

        # Fecha a tela atual
        self.root.destroy()

        # Abre a nova tela com base no tipo de usuário
        if tipo == "Administrador":
            self.abrir_tela_admin()
        else:
            self.abrir_tela_torcedor()

    def abrir_tela_torcedor(self):
        # Cria uma nova janela para a tela do torcedor
        nova_janela = tk.Tk()
        nova_janela.title("Tela do Torcedor")
        nova_janela.geometry("1920x1080")

        label = tk.Label(nova_janela, text="Bem-vindo, Torcedor!", font=("Arial", 16))
        label.pack(pady=50)

        nova_janela.mainloop()

    def abrir_tela_admin(self):
        # Cria uma nova janela para a tela do administrador
        nova_janela = tk.Tk()
        nova_janela.title("Tela do Administrador")
        nova_janela.geometry("1920x1080")

        label = tk.Label(nova_janela, text="Bem-vindo, Administrador!", font=("Arial", 16))
        label.pack(pady=50)

        nova_janela.mainloop()

# Função principal para iniciar a aplicação
def main():
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()

if __name__ == "__main__":
    main()