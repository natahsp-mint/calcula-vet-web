import json
from pathlib import Path
from services.calculator import calculate_dose_mg

# 📍 descobrir automaticamente a pasta raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
DRUGS_FILE = BASE_DIR / "data" / "drugs.json"

def load_drugs():
    with open(DRUGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

drugs_db = load_drugs()

def get_drug_data(drug):
    return drugs_db.get(drug)

def calculate_protocol(drug, weight, chosen_dose=None):
    data = drugs_db.get(drug)

    if not data:
        return "Fármaco não encontrado."

    if data["type"] == "fixed":
        dose_mg = calculate_dose_mg(weight, data["dose_mg_por_kg"])

    elif data["type"] == "range":
        if chosen_dose is None:
            return None
        dose_mg = calculate_dose_mg(weight, chosen_dose)

    intervalo = data.get("intervalo_horas", "")
    via = data.get("via", "")
    duracao = data.get("duracao_dias", "")

    texto = f"Administrar {dose_mg} mg"
    if via:
        texto += f" via {via}"
    if intervalo:
        texto += f" a cada {intervalo}h"
    if duracao:
        texto += f" por {duracao} dias"

    return texto
