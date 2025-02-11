import json
from modelo.Time import Time

class PersistenciaTime:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PersistenciaTime, cls).__new__(cls)
        return cls._instance
    
    def salvar_times(times, arquivo="times.json"):
        with open(arquivo, "w") as f:
            json.dump([t.to_dict() for t in times], f, indent=4)
    
    def carregar_times(arquivo="times.json"):
        try:
            with open(arquivo, "r") as f:
                data = json.load(f)
            return [Time.from_dict(t) for t in data]
        except FileNotFoundError:
            return []  # Caso o arquivo não exista ainda