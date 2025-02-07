import json
from modelo.Time import Time

class TimeDAO:
    _instance = None

    @staticmethod
    def get_instance():
        if TimeDAO._instance is None:
            TimeDAO._instance = TimeDAO()
        return TimeDAO._instance

    def __init__(self):
        if TimeDAO._instance is not None:
            raise Exception("Singleton instance already created.")
        
        self.file_name = 'times.json'

    def save(self, times):
        times_data = []
        for time in times:
            times_data.append({
                'nome': time.nome,
                'tecnico': time.tecnico,
                'pontos': time.pontuacao,
                'jogadores': [jogador.nome for jogador in time.jogadores]
            })

        with open(self.file_name, 'w') as arquivo:
            json.dump(times_data, arquivo, indent=4)

    def load(self):
        try:
            with open(self.file_name, 'r') as arquivo:
                times_data = json.load(arquivo)
            return [Time(nome=time['nome'], tecnico=time['tecnico'], pontuacao=time['pontos']) for time in times_data]
        except FileNotFoundError:
            return []
