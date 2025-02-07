from modelo import Time
import json
import os

class ControladorCampeonato:
    def __init__(self):
        # Inicializa a lista de times
        self.times = []

    @staticmethod
    def carregar_times(arquivo):
        """Carrega os times a partir de um arquivo JSON."""
        times = []
        if os.path.exists(arquivo):
            with open(arquivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    time = Time(item['nome'], item['tecnico'])
                    times.append(time)
        return times

    def adicionar_time(self, nome, tecnico):
        """Adiciona um novo time."""
        time = Time(nome, tecnico)
        self.times.append(time)

    def salvar_times(self):
        """Salva os times no arquivo JSON."""
        data = [{'nome': time.nome, 'tecnico': time.tecnico} for time in self.times]
        with open("times_cadastrados.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def listar_times(self):
        """Retorna a lista de times."""
        return [str(time) for time in self.times]
