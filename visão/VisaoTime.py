from controle.ControleTime import ControleTime

class VisaoTime:
    @staticmethod
    def adicionar_time(time):
        times = ControleTime.carregar_times()
        times.append(time)
        ControleTime.salvar_times(times)
    
    @staticmethod
    def remover_time(nome):
        times = [t for t in ControleTime.carregar_times() if t.nome != nome]
        ControleTime.salvar_times(times)
    
    @staticmethod
    def adicionar_jogador_ao_time(nome_time, jogador):
        times = ControleTime.carregar_times()
        for time in times:
            if time.nome == nome_time:
                time.adicionar_jogador(jogador)
        ControleTime.salvar_times(times)