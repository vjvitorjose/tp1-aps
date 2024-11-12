class TelaTorcedor:
    def __init__(self, window, times_cadastrados):
        self.window = window
        self.times_cadastrados = times_cadastrados
        
        # Definindo o título e o tamanho da janela
        self.window.title("Tela Torcedor")
        self.window.geometry("400x400")
        
        # Criando os botões de opções
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

        # Exibir a lista de times cadastrados
        times = "\n".join([time.nome for time in self.times_cadastrados])
        messagebox.showinfo("Times Cadastrados", f"Times cadastrados:\n{times}")

    def verificar_tabela(self):
        messagebox.showinfo("Tabela", "Função para verificar tabela ainda não implementada.")
    
    def logout(self):
        self.window.destroy()
