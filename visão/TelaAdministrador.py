import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from modelo.Time import Time
from modelo.Jogador import Jogador
from modelo.Partida import Partida

import json
from tkinter import ttk

class TelaAdministrador:
    
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Tela de Administrador")
        
        self.times_cadastrados = []
        self.jogadores_adicionados = []
        self.jogos = []
        self.carregar_times() 
        self.cria_botao()

    def cria_botao(self):
        self.label_bem_vindo = tk.Label(self.window, text="Bem-vindo, Administrador!")
        self.label_bem_vindo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.btn_cadastrar_time = tk.Button(self.window, text="Cadastrar Time", command=self.cadastrar_time)
        self.btn_cadastrar_time.grid(row=1, column=0, padx=10, pady=5)

        self.btn_verificar_tabela = tk.Button(self.window, text="Cadastrar Jogador", command=self.adicionar_jogador)
        self.btn_verificar_tabela.grid(row=7, column=0, padx=10, pady=5)


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
        self.btn_logout.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

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

        self.btn_salvar_time = tk.Button(self.cadastro_window, text="Salvar Time", command=self.salvar_time)
        self.btn_salvar_time.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


    def adicionar_jogador(self):

        if hasattr(self, 'jogadores_window') and self.jogadores_window.winfo_exists():
            return  # Se a janela de jogadores já estiver aberta, não faz nada


        self.adicionar_jogador_window = tk.Toplevel(self.window)
        self.adicionar_jogador_window.title("Adicionar Jogadores")

        self.label_nome_jogador = tk.Label(self.adicionar_jogador_window, text="Nome do Jogador:")
        self.label_nome_jogador.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nome_jogador = tk.Entry(self.adicionar_jogador_window)
        self.entry_nome_jogador.grid(row=0, column=1, padx=10, pady=5)

        self.label_numero_jogador = tk.Label(self.adicionar_jogador_window, text="Número do Jogador:")
        self.label_numero_jogador.grid(row=1, column=0, padx=10, pady=5)
        self.entry_numero_jogador = tk.Entry(self.adicionar_jogador_window)
        self.entry_numero_jogador.grid(row=1, column=1, padx=10, pady=5)

        self.label_posicao_jogador = tk.Label(self.adicionar_jogador_window, text="Posição do Jogador:")
        self.label_posicao_jogador.grid(row=2, column=0, padx=10, pady=5)
        self.entry_posicao_jogador = tk.Entry(self.adicionar_jogador_window)
        self.entry_posicao_jogador.grid(row=2, column=1, padx=10, pady=5)

        
        self.btn_adicionar_jogador = tk.Button(self.adicionar_jogador_window, text="Adicionar Jogador", command=self.adicionar_jogador)
        self.btn_adicionar_jogador.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

 
        self.btn_salvar_time = tk.Button(self.adicionar_jogador_window, text="Salvar Time", command=self.confirmar_cadastro)
        self.btn_salvar_time.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


    def salvar_jogador(self):
        # Lógica para salvar o jogador
        nome = self.entry_nome_jogador.get()
        numero = self.entry_numero_jogador.get()
        posicao = self.entry_posicao_jogador.get()

        # Adiciona o jogador à lista de jogadores
        self.jogadores.append({'nome': nome, 'numero': numero, 'posicao': posicao})

        # Limpar campos de entrada
        self.entry_nome_jogador.delete(0, tk.END)
        self.entry_numero_jogador.delete(0, tk.END)
        self.entry_posicao_jogador.delete(0, tk.END)

        # Fechar a janela após salvar
        self.adicionar_jogador_window.destroy()
    
    def salvar_time(self):
        nome_time = self.entry_nome_time.get()
        nome_tecnico = self.entry_tecnico.get()

        time = {"nome_time": nome_time, "nome_tecnico": nome_tecnico}
        self.times_cadastrados.append(time)

        self.entry_nome_time.delete(0, tk.END)
        self.entry_tecnico.delete(0, tk.END)

     
        self.cadastro_window.destroy()

        self.salvar_times_em_arquivo( )  
        self.visualizar_times()


    def adicionar_jogador_lista(self):
        nome_jogador = self.entry_nome_jogador.get()
        numero_jogador = self.entry_numero_jogador.get()
        posicao_jogador = self.entry_posicao_jogador.get()

        if nome_jogador == "" or numero_jogador == "" or posicao_jogador == "":
            messagebox.showwarning("AVISO", "Todos os campos devem ser preenchidos!")
        else:
            jogador = {
                "NOME": nome_jogador,
                "NUMERO": numero_jogador,
                "POSIÇÃO": posicao_jogador
            }

            self.jogadores_adicionados.append(jogador)
            self.entry_nome_jogador.delete(0, tk.END)
            self.entry_numero_jogador.delete(0, tk.END)
            self.entry_posicao_jogador.delete(0, tk.END)

            messagebox.showinfo("SUCESSO", f"Jogador {nome_jogador} adicionado ao time!")

    def confirmar_cadastro(self):
        # Aqui você pode adicionar a lógica de confirmação do cadastro do time
        print("Time salvo com sucesso!")
        print(f"Nome do time: {self.nome_time}")
        print("Jogadores cadastrados:")
        for jogador in self.jogadores:
            print(f"Nome: {jogador['nome']}, Número: {jogador['numero']}, Posição: {jogador['posicao']}")
        # Fechar a janela de adicionar jogador
        self.adicionar_jogador_window.destroy()

    def salvar_times_em_arquivo(self):
        try:
             with open("times_cadastrados.json", "a") as file:
                json.dump(self.times_cadastrados, file, indent=4)
                file.write("\n") 
        except Exception as e:
            messagebox.showerror("ERRO", f"Erro ao salvar o time: {str(e)}")
    

    def carregar_times(self):
        try:
            with open('times_cadastrados.json', 'r') as file:
                times = [] 
                for line in file:
                    try:
                        times.append(json.loads(line))  
                    except json.JSONDecodeError:
                        pass  # Se a linha não for válida, ignora
                self.times_cadastrados = [time for sublist in times for time in sublist]  # Achata a lista
                print(f"Times carregados: {self.times_cadastrados}")  # Exibe os times no console para depuração
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de times não encontrado.")
            self.times_cadastrados = []  # Inicializa como vazio em caso de arquivo não encontrado
        except Exception as e:
            messagebox.showerror("Erro desconhecido", f"Erro inesperado: {e}")
            self.times_cadastrados = []  # Inicializa como vazio em caso de erro inesperado

    def visualizar_times(self):
        if not self.times_cadastrados:
            messagebox.showinfo("AVISO", "Não há times cadastrados.")
        else:
            times_window = tk.Toplevel(self.window)
            times_window.title("Times Cadastrados")

            tree = ttk.Treeview(times_window, columns=("Nome do Time", "Técnico"), show="headings")
            tree.heading("Nome do Time", text="Nome do Time")
            tree.heading("Técnico", text="Técnico")

            for time in self.times_cadastrados:
                tree.insert("", tk.END, values=(time['nome_time'], time['nome_tecnico']))

            tree.pack()

    def remover_time(self):
        if not self.times_cadastrados:
            messagebox.showinfo("AVISO", "Não há times cadastrados.")
            return
        
        self.remover_window = tk.Toplevel(self.window)
        self.remover_window.title("Remover Time")
        
        self.label_selecionar_time = tk.Label(self.remover_window, text="Selecione um time para remover:")
        self.label_selecionar_time.grid(row=0, column=0, padx=10, pady=10)

        self.lista_times = tk.Listbox(self.remover_window)
        for time in self.times_cadastrados:
            self.lista_times.insert(tk.END, time['nome_time'])  
        self.lista_times.grid(row=1, column=0, padx=10, pady=10)

        self.btn_remover = tk.Button(self.remover_window, text="Remover Time", command=self.confirmar_remocao)
        self.btn_remover.grid(row=2, column=0, padx=10, pady=10)

    def confirmar_remocao(self):
        try:
            time_selecionado = self.lista_times.get(self.lista_times.curselection())

            time_para_remover = next(time for time in self.times_cadastrados if ['nome_time'] == time_selecionado)

            self.times_cadastrados.remove(time_para_remover)
            self.remover_window.destroy()
            messagebox.showinfo("SUCESSO",f"Time {time_selecionado} removido com sucesso!")

        except IndexError:
            messagebox.showwarning("AVISO" ,"Todos os campos devem ser preenchidos!")

    def atualizar_time(self):
        if not self.times_cadastrados:
            messagebox.showinfo("AVISO", "Não há times cadastrados para atualizar.")
            return

        self.atualizar_window = tk.Toplevel(self.window)
        self.atualizar_window.title("Atualizar Time")

        self.label_selecionar_time = tk.Label(self.atualizar_window, text="Selecione um time para atualizar:")
        self.label_selecionar_time.grid(row=0, column=0, padx=10, pady=10)

        print("Times cadastrados:", self.times_cadastrados)  

        self.lista_times = tk.Listbox(self.atualizar_window)
        for time in self.times_cadastrados:
            print(f"Inserindo time: {time}")  
            if 'nome_time' in time:
                self.lista_times.insert(tk.END, time['nome_time'])  
                print(f"Não esta listado {time}")

        self.lista_times.grid(row=1, column=0, padx=10, pady=10)

        self.btn_editar = tk.Button(self.atualizar_window, text="Editar Time", command=self.editar_time)
        self.btn_editar.grid(row=2, column=0, padx=10, pady=10)


    def editar_time(self):
        try:
            time_selecionado = self.lista_times.get(self.lista_times.curselection())
            time_para_editar = next(time for time in self.times_cadastrados if ['nome_time'] == time_selecionado)

            self.editar_window = tk.Toplevel(self.atualizar_window)
            self.editar_window.title(f"Editar Time: {time_selecionado}")

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
            for jogador in time_para_editar['jogadores']:
                self.lista_jogadores.insert(tk.END, jogador['nome'])
            self.lista_jogadores.grid(row=5, column=0, padx=10, pady=5)

            self.btn_remover_jogador = tk.Button(self.editar_window, text="Remover Jogador", command=lambda: self.remover_jogador(time_para_editar))
            self.btn_remover_jogador.grid(row=6, column=0, padx=10, pady=5)

        except IndexError:
            messagebox.showwarning("AVISO" ,"Todos os campos devem ser preenchidos!")

    def adicionar_jogador_editar(self):
        nome_jogador = self.entry_nome_jogador.get()
        numero_jogador = self.entry_numero_jogador.get()
        posicao_jogador = self.entry_posicao_jogador.get()

        if nome_jogador == "" or numero_jogador == "" or posicao_jogador == "":
            messagebox.showwarning("AVISO" ,"Todos os campos devem ser preenchidos!")        
        else:
            time_selecionado = self.lista_times.get(self.lista_times.curselection())
            time_para_editar = next(time for time in self.times_cadastrados if time.nome == time_selecionado)
            
            jogador = Jogador(nome_jogador, numero_jogador, posicao_jogador)
            time_para_editar.addJogador(jogador)
            
            self.editar_window.destroy()
            messagebox.showinfo("SUCESSO",f"Jogador {nome_jogador} adicionado ao time {time_selecionado}!")

    def remover_jogador(self, time):
        # Verifica se um item foi selecionado na lista
        selecionado = self.lista_jogadores.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um jogador para remover.")
            return

  
        jogador_selecionado = self.lista_jogadores.get(selecionado)
        
        jogador_para_remover = next((jogador for jogador in time.jogadores if jogador.nome == jogador_selecionado), None)

        if jogador_para_remover:
       
            time.removeJogador(jogador_para_remover)
            
            self.lista_jogadores.delete(selecionado)
            
            messagebox.showinfo("SUCESSO", f"Jogador {jogador_selecionado} removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Jogador não encontrado.")

  
    def adicionar_jogo(self):
        jogo_window = tk.Toplevel(self.window)  
        jogo_window.title("Adicionar Jogo")
        jogo_window.geometry("500x500")

        # Label e Listbox para a Equipe 1
        label_equipe1 = tk.Label(jogo_window, text="Equipe 1:")
        label_equipe1.grid(row=0, column=0, padx=10, pady=5)
        lista_equipe1 = tk.Listbox(jogo_window, selectmode=tk.SINGLE, height=5)  # Modo SINGLE para selecionar uma equipe por vez
        for time in self.times_cadastrados:
            lista_equipe1.insert(tk.END, time['nome_time'])
        lista_equipe1.grid(row=0, column=1, padx=10, pady=5)

        # Label e Listbox para a Equipe 2
        label_equipe2 = tk.Label(jogo_window, text="Equipe 2:")
        label_equipe2.grid(row=1, column=0, padx=10, pady=5)
        lista_equipe2 = tk.Listbox(jogo_window, selectmode=tk.SINGLE, height=5)  # Modo SINGLE para selecionar uma equipe por vez
        for time in self.times_cadastrados:
            lista_equipe2.insert(tk.END, time['nome_time'])
        lista_equipe2.grid(row=1, column=1, padx=10, pady=5)

        # Label e Entry para o placar
        label_placar = tk.Label(jogo_window, text="Placar (Equipe 1 x Equipe 2):")
        label_placar.grid(row=2, column=0, padx=10, pady=5)
        entry_placar1 = tk.Entry(jogo_window, width=5)
        entry_placar1.grid(row=2, column=1, padx=5, pady=5, sticky="W")
        label_x = tk.Label(jogo_window, text="x")
        label_x.grid(row=2, column=1, padx=5, pady=5)
        entry_placar2 = tk.Entry(jogo_window, width=5)
        entry_placar2.grid(row=2, column=1, padx=5, pady=5, sticky="E")

        # Label e Entry para a data
        label_data = tk.Label(jogo_window, text="Data do Jogo:")
        label_data.grid(row=3, column=0, padx=10, pady=5)
        entry_data = tk.Entry(jogo_window)
        entry_data.grid(row=3, column=1, padx=10, pady=5)

        def confirmar_jogo():
            selecao_equipe1 = lista_equipe1.curselection()
            selecao_equipe2 = lista_equipe2.curselection()

            if not selecao_equipe1 or not selecao_equipe2:
                messagebox.showwarning("Aviso", "Selecione uma equipe para cada lado.")
                return

            equipe1 = lista_equipe1.get(selecao_equipe1)  # Equipe 1
            equipe2 = lista_equipe2.get(selecao_equipe2)  # Equipe 2

            if equipe1 == equipe2:
                messagebox.showwarning("Aviso", "As equipes não podem ser as mesmas.")
                return

            placar1 = entry_placar1.get()
            placar2 = entry_placar2.get()
            data = entry_data.get()

            if not placar1 or not placar2 or not data:
                messagebox.showwarning("Aviso", "Preencha todos os campos corretamente.")
                return

            # Criar o dicionário do jogo
            jogo = {
                "equipe1": equipe1,
                "equipe2": equipe2,
                "placar1": placar1,
                "placar2": placar2,
                "data": data
            }

            # Salvar o jogo no arquivo
            with open("jogos.json", "a") as file:
                json.dump(jogo, file)
                file.write("\n")

            messagebox.showinfo("Sucesso", "Jogo salvo com sucesso!")
            jogo_window.destroy()  # Fechar a janela

            # Botão para confirmar e salvar o jogo
            btn_confirmar_jogo = tk.Button(jogo_window, text="Adicionar Jogo", command=confirmar_jogo)
            btn_confirmar_jogo.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


        
    def verificar_tabela(self):

        tabela_window = tk.Toplevel() 
        tree = ttk.Treeview(tabela_window, columns=("Time", "Pontos"))
        tree.heading("#1", text="Time")  # Cabeçalho da primeira coluna
        tree.heading("#2", text="Pontos")
        tree.grid(row=0, column=0, padx=10, pady=10)

        # Adiciona os jogos na tabela
        for jogo in self.jogos:
            tree.insert("", tk.END, values=(jogo.time1, f"{jogo.placar1} x {jogo.placar2}", jogo.time2, jogo.data_jogo, jogo.resultado_jogo))

    def logout(self):
        self.window.quit()
        self.window.destroy()

    def run(self):
        self.window.mainloop()