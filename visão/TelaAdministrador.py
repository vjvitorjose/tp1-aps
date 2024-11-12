import tkinter as tk
from tkinter import messagebox
from modelo.Time import Time
from modelo.Jogador import Jogador

class TelaAdministrador:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tela de Administrador")
        
        self.times_cadastrados = []
        
        self.create_widgets()

    def create_widgets(self):
        self.label_bem_vindo = tk.Label(self.window, text="Bem-vindo, Administrador!")
        self.label_bem_vindo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.btn_cadastrar_time = tk.Button(self.window, text="Cadastrar Time", command=self.cadastrar_time)
        self.btn_cadastrar_time.grid(row=1, column=0, padx=10, pady=5)

        self.btn_atualizar_time = tk.Button(self.window, text="Atualizar Time", command=self.atualizar_time)
        self.btn_atualizar_time.grid(row=2, column=0, padx=10, pady=5)

        self.btn_remover_time = tk.Button(self.window, text="Remover Time", command=self.remover_time)
        self.btn_remover_time.grid(row=3, column=0, padx=10, pady=5)

        self.btn_visualizar_time = tk.Button(self.window, text="Visualizar Times", command=self.visualizar_times)
        self.btn_visualizar_time.grid(row=4, column=0, padx=10, pady=5)

        self.btn_adicionar_jogo = tk.Button(self.window, text="Adicionar Jogo", command=self.adicionar_jogo)
        self.btn_adicionar_jogo.grid(row=5, column=0, padx=10, pady=5)

        self.btn_verificar_tabela = tk.Button(self.window, text="Verificar Tabela", command=self.verificar_tabela)
        self.btn_verificar_tabela.grid(row=6, column=0, padx=10, pady=5)

        self.btn_logout = tk.Button(self.window, text="Logout", command=self.logout)
        self.btn_logout.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar_time(self):
        self.cadastro_window = tk.Toplevel(self.window)
        self.cadastro_window.title("Cadastro de Time")

        self.label_nome_time = tk.Label(self.cadastro_window, text="Nome do Time:")
        self.label_nome_time.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nome_time = tk.Entry(self.cadastro_window)
        self.entry_nome_time.grid(row=0, column=1, padx=10, pady=5)

        self.label_tecnico = tk.Label(self.cadastro_window, text="Nome do Técnico:")
        self.label_tecnico.grid(row=1, column=0, padx=10, pady=5)
        self.entry_tecnico = tk.Entry(self.cadastro_window)
        self.entry_tecnico.grid(row=1, column=1, padx=10, pady=5)

        self.label_nome_jogador = tk.Label(self.cadastro_window, text="Nome do Jogador:")
        self.label_nome_jogador.grid(row=2, column=0, padx=10, pady=5)
        self.entry_nome_jogador = tk.Entry(self.cadastro_window)
        self.entry_nome_jogador.grid(row=2, column=1, padx=10, pady=5)

        self.label_numero_jogador = tk.Label(self.cadastro_window, text="Número do Jogador:")
        self.label_numero_jogador.grid(row=3, column=0, padx=10, pady=5)
        self.entry_numero_jogador = tk.Entry(self.cadastro_window)
        self.entry_numero_jogador.grid(row=3, column=1, padx=10, pady=5)

        self.label_posicao_jogador = tk.Label(self.cadastro_window, text="Posição do Jogador:")
        self.label_posicao_jogador.grid(row=4, column=0, padx=10, pady=5)
        self.entry_posicao_jogador = tk.Entry(self.cadastro_window)
        self.entry_posicao_jogador.grid(row=4, column=1, padx=10, pady=5)

        self.btn_adicionar_jogador = tk.Button(self.cadastro_window, text="Adicionar Jogador", command=self.adicionar_jogador)
        self.btn_adicionar_jogador.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.btn_confirmar = tk.Button(self.cadastro_window, text="Cadastrar Time", command=self.confirmar_cadastro)
        self.btn_confirmar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.jogadores_adicionados = []  # Lista de jogadores adicionados

    def adicionar_jogador(self):
        nome_jogador = self.entry_nome_jogador.get()
        numero_jogador = self.entry_numero_jogador.get()
        posicao_jogador = self.entry_posicao_jogador.get()

        if nome_jogador == "" or numero_jogador == "" or posicao_jogador == "":
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos do jogador.")
        else:
            jogador = Jogador(nome_jogador, numero_jogador, posicao_jogador)
            self.jogadores_adicionados.append(jogador)
            
            self.entry_nome_jogador.delete(0, tk.END)
            self.entry_numero_jogador.delete(0, tk.END)
            self.entry_posicao_jogador.delete(0, tk.END)
            
            messagebox.showinfo("Sucesso", f"Jogador {nome_jogador} adicionado ao time!")

    def confirmar_cadastro(self):
        nome_time = self.entry_nome_time.get()
        nome_tecnico = self.entry_tecnico.get()

        if nome_time == "" or nome_tecnico == "":
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos do time.")
        else:
            time = Time(nome_time, nome_tecnico)
            for jogador in self.jogadores_adicionados:
                time.addJogador(jogador)

            self.times_cadastrados.append(time)
            
            self.cadastro_window.destroy()
            
            messagebox.showinfo("Sucesso", f"Time {nome_time} cadastrado com sucesso!")

    def visualizar_times(self):
        if not self.times_cadastrados:
            messagebox.showinfo("Nenhum Time Cadastrado", "Não há times cadastrados.")
        else:
            times_info = "\n".join([f"{time.nome} - Técnico: {time.tecnico}" for time in self.times_cadastrados])
            messagebox.showinfo("Times Cadastrados", f"Times cadastrados:\n{times_info}")

    def remover_time(self):
        if not self.times_cadastrados:
            messagebox.showinfo("Nenhum Time Cadastrado", "Não há times cadastrados para remover.")
            return
        
        self.remover_window = tk.Toplevel(self.window)
        self.remover_window.title("Remover Time")
        
        self.label_selecionar_time = tk.Label(self.remover_window, text="Selecione um time para remover:")
        self.label_selecionar_time.grid(row=0, column=0, padx=10, pady=10)

        self.lista_times = tk.Listbox(self.remover_window)
        for time in self.times_cadastrados:
            self.lista_times.insert(tk.END, time.nome)
        self.lista_times.grid(row=1, column=0, padx=10, pady=10)

        self.btn_remover = tk.Button(self.remover_window, text="Remover Time", command=self.confirmar_remocao)
        self.btn_remover.grid(row=2, column=0, padx=10, pady=10)

    def confirmar_remocao(self):
        try:
            time_selecionado = self.lista_times.get(self.lista_times.curselection())

            time_para_remover = next(time for time in self.times_cadastrados if time.nome == time_selecionado)

            self.times_cadastrados.remove(time_para_remover)
            self.remover_window.destroy()
            messagebox.showinfo("Sucesso", f"Time {time_selecionado} removido com sucesso!")

        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um time para remover.")

    def atualizar_time(self):
        if not self.times_cadastrados:
            messagebox.showinfo("Nenhum Time Cadastrado", "Não há times cadastrados para atualizar.")
            return
        
        self.atualizar_window = tk.Toplevel(self.window)
        self.atualizar_window.title("Atualizar Time")
        
        self.label_selecionar_time = tk.Label(self.atualizar_window, text="Selecione um time para atualizar:")
        self.label_selecionar_time.grid(row=0, column=0, padx=10, pady=10)

        self.lista_times = tk.Listbox(self.atualizar_window)
        for time in self.times_cadastrados:
            self.lista_times.insert(tk.END, time.nome)
        self.lista_times.grid(row=1, column=0, padx=10, pady=10)

        self.btn_editar = tk.Button(self.atualizar_window, text="Editar Time", command=self.editar_time)
        self.btn_editar.grid(row=2, column=0, padx=10, pady=10)

    def editar_time(self):
        try:
            time_selecionado = self.lista_times.get(self.lista_times.curselection())
            time_para_editar = next(time for time in self.times_cadastrados if time.nome == time_selecionado)

            self.editar_window = tk.Toplevel(self.atualizar_window)
            self.editar_window.title(f"Editar Time {time_selecionado}")

            self.label_nome_jogador = tk.Label(self.editar_window, text="Nome do Jogador:")
            self.label_nome_jogador.grid(row=0, column=0, padx=10, pady=5)
            self.entry_nome_jogador = tk.Entry(self.editar_window)
            self.entry_nome_jogador.grid(row=0, column=1, padx=10, pady=5)

            self.label_numero_jogador = tk.Label(self.editar_window, text="Número do Jogador:")
            self.label_numero_jogador.grid(row=1, column=0, padx=10, pady=5)
            self.entry_numero_jogador = tk.Entry(self.editar_window)
            self.entry_numero_jogador.grid(row=1, column=1, padx=10, pady=5)

            self.label_posicao_jogador = tk.Label(self.editar_window, text="Posição do Jogador:")
            self.label_posicao_jogador.grid(row=2, column=0, padx=10, pady=5)
            self.entry_posicao_jogador = tk.Entry(self.editar_window)
            self.entry_posicao_jogador.grid(row=2, column=1, padx=10, pady=5)

            self.btn_adicionar_jogador = tk.Button(self.editar_window, text="Adicionar Jogador", command=self.adicionar_jogador_editar)
            self.btn_adicionar_jogador.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

            self.label_remover_jogador = tk.Label(self.editar_window, text="Selecione um jogador para remover:")
            self.label_remover_jogador.grid(row=4, column=0, padx=10, pady=5)

            self.lista_jogadores = tk.Listbox(self.editar_window)
            for jogador in time_para_editar.jogadores:
                self.lista_jogadores.insert(tk.END, jogador.nome)
            self.lista_jogadores.grid(row=5, column=0, padx=10, pady=5)

            self.btn_remover_jogador = tk.Button(self.editar_window, text="Remover Jogador", command=lambda: self.remover_jogador(time_para_editar))
            self.btn_remover_jogador.grid(row=6, column=0, padx=10, pady=5)

        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um time para editar.")

    def adicionar_jogador_editar(self):
        nome_jogador = self.entry_nome_jogador.get()
        numero_jogador = self.entry_numero_jogador.get()
        posicao_jogador = self.entry_posicao_jogador.get()

        if nome_jogador == "" or numero_jogador == "" or posicao_jogador == "":
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos do jogador.")
        else:
            time_selecionado = self.lista_times.get(self.lista_times.curselection())
            time_para_editar = next(time for time in self.times_cadastrados if time.nome == time_selecionado)
            
            jogador = Jogador(nome_jogador, numero_jogador, posicao_jogador)
            time_para_editar.addJogador(jogador)
            
            self.editar_window.destroy()
            messagebox.showinfo("Sucesso", f"Jogador {nome_jogador} adicionado ao time {time_selecionado}!")

    def remover_jogador(self, time):
        jogador_selecionado = self.lista_jogadores.get(self.lista_jogadores.curselection())
        jogador_para_remover = next((jogador for jogador in time.jogadores if jogador.nome == jogador_selecionado), None)

        if jogador_para_remover:
            time.removeJogador(jogador_para_remover)
            messagebox.showinfo("Sucesso", f"Jogador {jogador_selecionado} removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Jogador não encontrado.")

    def adicionar_jogo(self):
        messagebox.showinfo("Adicionar Jogo", "Opção para adicionar jogo (implementação futura).")

    def verificar_tabela(self):
        messagebox.showinfo("Verificar Tabela", "Opção para verificar tabela (implementação futura).")

    def logout(self):
        self.window.quit()
        self.window.destroy()

    def run(self):
        self.window.mainloop()