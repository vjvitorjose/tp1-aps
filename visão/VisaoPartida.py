from controle.ControlePartida import ControlePartida

class VisaoPartida:
    @staticmethod
    def adicionar_partida(partida):
        partidas = ControlePartida.carregar_partidas()
        partidas.append(partida)
        ControlePartida.salvar_partidas(partidas)
    
    @staticmethod
    def remover_partida(index):
        partidas = ControlePartida.carregar_partidas()
        if 0 <= index < len(partidas):
            del partidas[index]
        ControlePartida.salvar_partidas(partidas)
    
    @staticmethod
    def definir_placar(index, gols_casa, gols_visitante):
        partidas = ControlePartida.carregar_partidas()
        if 0 <= index < len(partidas):
            partidas[index].definir_placar(gols_casa, gols_visitante)
        ControlePartida.salvar_partidas(partidas)