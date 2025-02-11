from controle.ControleJogador import ControleJogador

class VisaoJogador:
    @staticmethod
    def adicionar_jogador(jogador):
        jogadores = ControleJogador.carregar_jogadores()
        jogadores.append(jogador)
        ControleJogador.salvar_jogadores(jogadores)
    
    @staticmethod
    def remover_jogador(nome):
        jogadores = [j for j in ControleJogador.carregar_jogadores() if j.nome != nome]
        ControleJogador.salvar_jogadores(jogadores)