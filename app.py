import streamlit as st
from services.drug_service import (
    load_drugs,
    get_drug_data,
    needs_species,
    needs_indication,
    needs_range,
    resolve_dose_node,
    calculate_protocol
)


st.title("🐾 Bem-vindo ao Calcula Vet")

# carregar banco atualizado
drugs_db = load_drugs()

# lista automática de fármacos
drug_list = sorted(list(drugs_db.keys()))

# lista automática de fármacos
drug_list = sorted(list(drugs_db.keys()))
drug = st.selectbox("Escolha o fármaco:", drug_list)

weight = st.number_input("Peso do paciente (kg)", min_value=0.1)

drug_data = get_drug_data(drug)

species = None
indication = None
chosen_dose = None

# 🧠 2) perguntar espécie se necessário
if needs_species(drug_data):
    species = st.selectbox(
        "Espécie:",
        list(drug_data["species"].keys())
    )

# 🧠 3) perguntar indicação se necessário
if species and needs_indication(drug_data, species):
    indication = st.selectbox(
        "Indicação:",
        list(drug_data["species"][species]["indications"].keys())
    )

# 🧠 4) descobrir o nó final da dose
if drug:
    if needs_species(drug_data) and not species:
        st.stop()

    if species and needs_indication(drug_data, species) and not indication:
        st.stop()

    dose_data = resolve_dose_node(drug, species, indication)

    # 🧠 5) perguntar dose se for RANGE
    if needs_range(dose_data):
        chosen_dose = st.number_input(
            f"Escolha a dose ({dose_data['min']} – {dose_data['max']} mg/kg)",
            min_value=float(dose_data["min"]),
            max_value=float(dose_data["max"])
        )
    else:
        chosen_dose = dose_data["value"]

# 🧮 6) botão calcular
if st.button("Calcular dose"):
    if weight <= 0:
        st.error("Informe o peso.")
        st.stop()

    if chosen_dose is None:
        st.error("Complete as informações.")
        st.stop()

    resultado = calculate_protocol(
        drug,
        weight,
        chosen_dose,
        species,
        indication
    )

    st.success(resultado)

st.divider()
<<<<<<< HEAD
st.caption("Este material serve de apoio e não dispensa julgamento clínico, utilize por sua conta e risco.")
=======
st.caption("Este material é baseado na 4ª Edição do Guia Terapêutico Veterinário e serve de apoio, não dispensando julgamento clínico. Utilize por sua conta e risco.")
>>>>>>> 4ac0976 (organizes drugs.json)
