import json
from modelo.Time import Time

class ControleTime:
    
    @staticmethod
    def salvar_times(times, arquivo="times.json"):
        with open(arquivo, "w") as f:
            json.dump([t.to_dict() for t in times], f, indent=4)
    
    @staticmethod
    def carregar_times(arquivo="times.json"):
        try:
            with open(arquivo, "r") as f:
                data = json.load(f)
            return [Time.from_dict(t) for t in data]
        except FileNotFoundError:
            return []  # Caso o arquivo não exista ainda
