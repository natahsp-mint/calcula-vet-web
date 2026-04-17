import streamlit as st

st.set_page_config(page_title="Calcula Vet", page_icon="🐾")

st.title("🐾 Calcula Vet")
st.write("Calculadora veterinária de doses")

peso = st.number_input("Digite o peso do animal (kg)", min_value=0.0, step=0.1)

farmaco = st.selectbox(
    "Escolha o fármaco",
    ["Meloxicam", "Dipirona", "Omeprazol"]
)

especie = st.selectbox(
    "Escolha a espécie",
    ["Cão", "Gato"]
)

if st.button("Calcular"):
    dose = 0.0
    recomendacao = ""

    if farmaco == "Meloxicam":
        if especie == "Cão":
            dose = 0.1 * peso
            recomendacao = f"Iniciar com {0.2 * peso:.2f} mg e continuar com {dose:.2f} mg SID."
        else:
            dose = 0.05 * peso
            recomendacao = f"Iniciar com {0.1 * peso:.2f} mg e continuar com {dose:.2f} mg SID."

    elif farmaco == "Dipirona":
        dose = 25 * peso
        recomendacao = f"Administrar {dose:.2f} mg a cada 8–12 horas."

    elif farmaco == "Omeprazol":
        dose = 1 * peso
        recomendacao = f"Administrar {dose:.2f} mg SID."

    st.subheader("Resultado")
    st.write(recomendacao)
