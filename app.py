import streamlit as st
from services.drug_service import get_drug_data, calculate_protocol

st.title("💊 Calculadora Veterinária")

drug = st.selectbox(
    "Escolha o fármaco",
    [
        "Albendazol","Alopurinol","Alprazolam","Amoxicilina","Dipirona",
        "Doxiciclina","Enrofloxacina","Maropitant","Meloxicam",
        "Metronidazol","Omeprazol","Prednisolona"
    ]
)

weight = st.number_input("Peso do paciente (kg)", min_value=0.1)

drug_key = drug.lower()
data = get_drug_data(drug_key)

chosen_dose = None

# ⭐ SE FOR DOSE EM FAIXA → MOSTRA SLIDER
if data and data["type"] == "range":
    st.warning("Este fármaco possui dose em faixa.")
    chosen_dose = st.slider(
        "Escolha a dose (mg/kg)",
        data["min_mg_por_kg"],
        data["max_mg_por_kg"],
        (data["min_mg_por_kg"] + data["max_mg_por_kg"]) / 2
    )

if st.button("Calcular"):
    resultado = calculate_protocol(drug_key, weight, chosen_dose)
    st.success(resultado)
