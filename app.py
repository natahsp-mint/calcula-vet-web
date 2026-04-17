import streamlit as st
import unicodedata


def normalize_drug_name(drug_name):
    lowered_name = drug_name.lower()
    return "".join(
        char for char in unicodedata.normalize("NFD", lowered_name)
        if unicodedata.category(char) != "Mn"
    )


def calculate_dose_mg(weight, mg_per_kg):
    return weight * mg_per_kg


st.set_page_config(page_title="Calcula Vet", page_icon="🐾")

st.title("🐾 Calcula Vet")
st.write("A calculadora baseada no Guia Terapêutico Veterinário 4ª Edição.")

# entrada principal
weight = st.number_input("Digite o peso do animal:", min_value=0.0, step=0.1)
drug_input = st.text_input("Digite o nome do princípio ativo:")
drug = normalize_drug_name(drug_input) if drug_input else ""

resultado = ""

# amoxicilina
if drug == "amoxicilina":
    dosage = st.number_input(
        "Digite a dosagem desejada entre 10-20 mg/kg:",
        min_value=10.0,
        max_value=20.0,
        step=0.1,
        key="amoxicilina_dosage"
    )

    if st.button("Calcular", key="btn_amoxicilina"):
        dose = calculate_dose_mg(weight, dosage)
        resultado = f"Administrar {dose:.2f} mg IM/SC/VO a cada 8-12 horas."

# dipirona
elif drug == "dipirona":
    if st.button("Calcular", key="btn_dipirona"):
        dose = calculate_dose_mg(weight, 25)
        resultado = f"Administrar {dose:.2f} mg IV/IM/SC/VO a cada 8 horas."

# doxiciclina
elif drug == "doxiciclina":
    if st.button("Calcular", key="btn_doxiciclina"):
        dose = calculate_dose_mg(weight, 10)
        resultado = f"Administrar {dose:.2f} mg IV/VO a cada 12-24 horas."

# enrofloxacina / enrofloxacino
elif drug in ("enrofloxacina", "enrofloxacino"):
    species = st.selectbox(
        "Selecione a espécie:",
        ["Cão", "Gato"],
        key="enro_species"
    )

    if species == "Cão":
        dosage = st.number_input(
            "Digite a dosagem desejada entre 5-10 mg/kg:",
            min_value=5.0,
            max_value=10.0,
            step=0.1,
            key="enro_dog_dosage"
        )

    if st.button("Calcular", key="btn_enrofloxacina"):
        if species == "Cão":
            dose = calculate_dose_mg(weight, dosage)
            resultado = f"Administrar {dose:.2f} mg IM/VO a cada 12-24 horas."
        elif species == "Gato":
            dose = calculate_dose_mg(weight, 2.5)
            resultado = f"Administrar {dose:.2f} mg VO a cada 12 horas."

# maropitant
elif drug in ("maropitant", "maropitante"):
    if st.button("Calcular", key="btn_maropitant"):
        resultado = f"Administrar {weight:.2f} mg SC/VO SID."

# meloxicam
elif drug == "meloxicam":
    species = st.selectbox(
        "Selecione a espécie:",
        ["Cão", "Gato"],
        key="meloxicam_species"
    )

    if st.button("Calcular", key="btn_meloxicam"):
        if species == "Cão":
            dose = calculate_dose_mg(weight, 0.1)
            resultado = (
                f"Iniciar com {calculate_dose_mg(weight, 0.2):.2f} mg IV/SC/VO, "
                f"continuando com {dose:.2f} mg VO SID."
            )
        elif species == "Gato":
            dose = calculate_dose_mg(weight, 0.05)
            resultado = (
                f"Iniciar com {calculate_dose_mg(weight, 0.1):.2f} mg SC/VO, "
                f"continuando com {dose:.2f} mg VO SID. "
                f"Pode também ser usada uma dose única de {calculate_dose_mg(weight, 0.3):.2f} mg."
            )

# metronidazol
elif drug == "metronidazol":
    case = st.selectbox(
        "Selecione a indicação:",
        ["Giardíase", "Anaeróbicos"],
        key="metro_case"
    )

    if st.button("Calcular", key="btn_metronidazol"):
        if case == "Giardíase":
            dose = calculate_dose_mg(weight, 25)
            resultado = f"Administrar {dose:.2f} mg BID ou {2 * dose:.2f} mg SID VO por 5 dias."
        elif case == "Anaeróbicos":
            dose = calculate_dose_mg(weight, 15)
            resultado = f"Administrar {dose:.2f} mg IV/VO BID."

# omeprazol
elif drug == "omeprazol":
    dosage = st.number_input(
        "Digite a dosagem desejada entre 0.5-1 mg/kg:",
        min_value=0.5,
        max_value=1.0,
        step=0.1,
        key="omeprazol_dosage"
    )

    if st.button("Calcular", key="btn_omeprazol"):
        dose = calculate_dose_mg(weight, dosage)
        resultado = f"Administrar {dose:.2f} mg VO SID."

# prednisolona
elif drug == "prednisolona":
    species = st.selectbox(
        "Selecione a espécie:",
        ["Cão", "Gato"],
        key="pred_species"
    )

    case = st.selectbox(
        "Selecione o caso:",
        ["Alergia", "Imunossupressão", "Uso prolongado"],
        key="pred_case"
    )

    if species == "Cão" and case == "Alergia":
        dosage = st.number_input(
            "Digite a dosagem desejada entre 0.5-1 mg/kg:",
            min_value=0.5,
            max_value=1.0,
            step=0.1,
            key="pred_dog_allergy"
        )

    elif species == "Cão" and case == "Uso prolongado":
        dosage = st.number_input(
            "Digite a dosagem desejada entre 0.5-2 mg/kg:",
            min_value=0.5,
            max_value=2.0,
            step=0.1,
            key="pred_dog_long"
        )

    elif species == "Gato" and case == "Uso prolongado":
        dosage = st.number_input(
            "Digite a dosagem desejada entre 2-4 mg/kg:",
            min_value=2.0,
            max_value=4.0,
            step=0.1,
            key="pred_cat_long"
        )

    if st.button("Calcular", key="btn_prednisolona"):
        if species == "Cão" and case == "Alergia":
            dose = calculate_dose_mg(weight, dosage)
            resultado = f"Administrar {dose:.2f} mg IM/VO BID."

        elif species == "Cão" and case == "Imunossupressão":
            dose = calculate_dose_mg(weight, 2)
            resultado = f"Administrar {dose:.2f} mg IM/VO BID."

        elif species == "Cão" and case == "Uso prolongado":
            dose = calculate_dose_mg(weight, dosage)
            resultado = f"Administrar {dose:.2f} mg VO em manhãs alternadas."

        elif species == "Gato" and case == "Alergia":
            dose = calculate_dose_mg(weight, 1)
            resultado = f"Administrar {dose:.2f} mg IM/VO BID."

        elif species == "Gato" and case == "Imunossupressão":
            dose = calculate_dose_mg(weight, 3)
            resultado = f"Administrar {dose:.2f} mg IM/VO BID."

        elif species == "Gato" and case == "Uso prolongado":
            dose = calculate_dose_mg(weight, dosage)
            resultado = f"Administrar {dose:.2f} mg VO em noites alternadas."

# princípio ativo inválido
elif drug_input:
    st.error("Princípio ativo inválido ou indisponível! Tente novamente.")

# resultado
if resultado:
    st.subheader("Resultado")
    st.success(resultado)