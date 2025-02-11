import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelo.Time import Time

import json

class ControleTime:
    @staticmethod
    def salvar_times(times, arquivo="times.json"):
        with open(arquivo, "w") as f:
            json.dump([t.to_dict() for t in times], f, indent=4)
    
    @staticmethod
    def carregar_times(arquivo="times.json"):
        with open(arquivo, "r") as f:
            data = json.load(f)
        return [Time.from_dict(t) for t in data]
    
times = []
time = Time("galo", "cuca")
times.append(time)
time = Time("flamengo", "ricardo")
times.append(time)
ControleTime.salvar_times(times)