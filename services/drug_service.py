import json
import os
from services.calculator import calculate_dose_mg


# caminho absoluto até /data/drugs.json
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "drugs.json"

def load_drugs():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

drugs_db = load_drugs()

# 🔎 obter dados da droga
def get_drug_data(drug):
    return drugs_db.get(drug)

# 🔎 verificar se precisa perguntar espécie
def needs_species(drug_data):
    return "species" in drug_data

# 🔎 verificar se precisa perguntar indicação
def needs_indication(drug_data, species):
    return "indications" in drug_data["species"][species]

# 🔎 verificar se precisa perguntar dose (range)
def needs_range(dose_data):
    return dose_data["type"] == "range"

# 🧠 encontrar o nó final da dose na árvore
def resolve_dose_node(drug, species=None, indication=None):
    data = drugs_db[drug]

    # se tiver espécie
    if "species" in data:
        data = data["species"][species]

    # se tiver indicação
    if "indications" in data:
        data = data["indications"][indication]

    return data["dose"]

# 💊 cálculo final
def calculate_protocol(drug, weight, chosen_dose, species=None, indication=None):
    dose_data = resolve_dose_node(drug, species, indication)

    mg_total = calculate_dose_mg(weight, chosen_dose)

    return (
        f"Administrar {mg_total} mg "
        f"{dose_data['route']} "
        f"a cada {dose_data['interval']}."
    )
