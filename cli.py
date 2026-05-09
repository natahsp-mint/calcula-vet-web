from services.drug_service import (
    get_drug_data,
    needs_species,
    needs_indication,
    needs_range,
    resolve_dose_node,
    calculate_protocol
)

def ask_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido.")

def choose_option(title, options):
    print(f"\n{title}")
    for i, opt in enumerate(options, 1):
        print(f"{i} - {opt}")
    
    while True:
        try:
            choice = int(input("Escolha uma opção: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print("Opção inválida.")

def main():
    print("\n🐾 Calculadora Veterinária CLI\n")

    # 🧠 lista de drogas (igual ao app.py)
    drug_list = [
        "maropitant",
        "amoxicilina",
        "meloxicam",
        "prednisolona"
    ]

    # 1️⃣ escolher droga
    drug = choose_option("Escolha o fármaco:", drug_list)
    drug_data = get_drug_data(drug)

    # 2️⃣ peso
    weight = ask_float("Peso do paciente (kg): ")

    species = None
    indication = None

    # 3️⃣ perguntar espécie se necessário
    if needs_species(drug_data):
        species = choose_option(
            "Escolha a espécie:",
            list(drug_data["species"].keys())
        )

    # 4️⃣ perguntar indicação se necessário
    if species and needs_indication(drug_data, species):
        indication = choose_option(
            "Escolha a indicação:",
            list(drug_data["species"][species]["indications"].keys())
        )

    # 5️⃣ descobrir dose final
    dose_data = resolve_dose_node(drug, species, indication)

    # 6️⃣ perguntar dose se for range
    if needs_range(dose_data):
        print(f"\nDose disponível: {dose_data['min']} – {dose_data['max']} mg/kg")
        chosen_dose = ask_float("Escolha a dose desejada: ")
    else:
        chosen_dose = dose_data["value"]

    # 7️⃣ calcular protocolo
    resultado = calculate_protocol(
        drug,
        weight,
        chosen_dose,
        species,
        indication
    )

    print("\n💊 Resultado:")
    print(resultado)
    print()

if __name__ == "__main__":
    main()