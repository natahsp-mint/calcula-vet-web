import unicodedata
import builtins


def normalized_input(prompt=""):
    return builtins.input(prompt).replace(",", ".")

#fix in case numeric value is asked and user mistakes the entry
def get_numeric_input(prompt):
    while True:
        try:
            return float(normalized_input(prompt))
        except ValueError:
            print("Resposta inválida! Tente novamente.")

#fix in case user types value out of given range
def get_dosage_in_range(prompt, min_value, max_value):
    while True:
        dosage = get_numeric_input(prompt)
        if min_value <= dosage <= max_value:
            return dosage
        print(f"Valor fora da faixa permitida ({min_value}-{max_value} mg/kg).")


def calculate_dose_mg(weight, mg_per_kg):
    return weight * mg_per_kg


def normalize_drug_name(drug_name):
    lowered_name = drug_name.lower()
    return "".join(
        char for char in unicodedata.normalize("NFD", lowered_name)
        if unicodedata.category(char) != "Mn"
    )


def run_cli():
    print("Bem-vindo ao Calcula Vet Web!")
    print("A calculadora baseada no Guia Terapêutico Veterinário 4ª Edição.")
    # asks for the weight of the animal and store it in a variable
    weight = get_numeric_input("Digite o peso do animal: ")
    # ask for the drug name and store it in a variable (retry if invalid)
    drug = normalize_drug_name(builtins.input("Digite o nome do princípio ativo: "))
    # call the dose variable and stores a float on it
    dose = 1.0

    # the user types amoxicilina
    if drug == "amoxicilina":
        dosage = get_dosage_in_range("Digite a dosagem desejada entre 10-20mg/kg: ", 10, 20)
        dose = calculate_dose_mg(weight, dosage)
        print(f"Administrar {dose}mg IM/SC/VO a cada 8-12 horas.")

    # the user types dipirona
    elif drug == "dipirona":
        dose = calculate_dose_mg(weight, 25)
        print(f"Administrar {dose}mg IV/IM/SC/VO a cada 8 horas.")

    # the user types doxiciclina
    elif drug == "doxiciclina":
        dose = calculate_dose_mg(weight, 10)
        print(f"Administrar {dose}mg IV/VO a cada 12-24 horas.")

    # the user types enrofloxacina / enrofloxacino
    elif drug in ("enrofloxacina", "enrofloxacino"):
        print("1 - Cão")
        print("2 - Gato")
        while True:
            species = builtins.input("Selecione a opção da espécie: ")
            if species == "1":
                dosage = get_dosage_in_range("Digite a dosagem desejada entre 5-10mg/kg: ", 5, 10)
                dose = calculate_dose_mg(weight, dosage)
                print(f"Administrar {dose}mg IM/VO a cada 12-24 horas.")
                break
            elif species == "2":
                dose = calculate_dose_mg(weight, 2.5)
                print(f"Administrar {dose}mg VO a cada 12 horas.")
                break
            print("Opção inválida. Escolha 1 (Cão) ou 2 (Gato).")

    # the user types maropitant
    elif drug in ("maropitant", "maropitante"):
        print(f"Administrar {weight}mg SC/VO SID")

    # the user types meloxicam
    elif drug == "meloxicam":
        print("1 - Cão")
        print("2 - Gato")
        while True:
            species = builtins.input("Selecione a opção da espécie: ")
            if species == "1":
                dose = calculate_dose_mg(weight, 0.1)
                print(f"Iniciar com {calculate_dose_mg(weight, 0.2)}mg IV/SC/VO, continuando com {dose}mg VO SID.")
                break
            elif species == "2":
                dose = calculate_dose_mg(weight, 0.05)
                print(f"Iniciar com {calculate_dose_mg(weight, 0.1)}mg SC/VO, continuando com {dose}mg VO SID. Pode também ser usada uma dose única de {calculate_dose_mg(weight, 0.3)}mg.")
                break
            print("Opção inválida. Escolha 1 (Cão) ou 2 (Gato).")

    # the user types metronidazol
    elif drug == "metronidazol":
        print("1 - Giardíase")
        print("2 - Anaeróbicos")
        while True:
            case = builtins.input("Digite a opção desejada: ")
            if case == "1":
                dose = calculate_dose_mg(weight, 25)
                print(f"Administrar {dose}mg BID ou {2 * dose}mg SID VO por 5 dias.")
                break
            elif case == "2":
                dose = calculate_dose_mg(weight, 15)
                print(f"Administrar {dose}mg IV/VO BID.")
                break
            print("Opção inválida. Escolha 1 ou 2.")

    # the user types omeprazol
    elif drug == "omeprazol":
        dosage = get_dosage_in_range("Digite a dosagem desejada entre 0.5-1mg/kg: ", 0.5, 1)
        dose = calculate_dose_mg(weight, dosage)
        print(f"Administrar {dose}mg VO SID.")

    # the user types prednisolona
    elif drug == "prednisolona":
        while True:
            print("1 - Cão")
            print("2 - Gato")
            species = builtins.input("Selecione a espécie (digite apenas o número): ")
            print("1 - Alergia")
            print("2 - Imunossupressão")
            print("3 - Uso prolongado")
            case = builtins.input("Selecione o caso (digite apenas o número): ")
            if species == "1" and case == "1":
                dosage = get_dosage_in_range("Digite a dosagem desejada entre 0.5-1mg/kg: ", 0.5, 1)
                dose = calculate_dose_mg(weight, dosage)
                print(f"Administrar {dose}mg IM/VO BID.")
                break
            elif species == "1" and case == "2":
                dose = calculate_dose_mg(weight, 2)
                print(f"Administrar {dose}mg IM/VO BID.")
                break
            elif species == "1" and case == "3":
                dosage = get_dosage_in_range("Digite a dosagem desejada entre 0.5-2mg/kg: ", 0.5, 2)
                dose = calculate_dose_mg(weight, dosage)
                print(f"Administrar {dose}mg VO em manhãs alternadas.")
                break
            elif species == "2" and case == "1":
                dose = calculate_dose_mg(weight, 1)
                print(f"Administrar {dose}mg IM/VO BID.")
                break
            elif species == "2" and case == "2":
                dose = calculate_dose_mg(weight, 3)
                print(f"Administrar {dose}mg IM/VO BID.")
                break
            elif species == "2" and case == "3":
                dosage = get_dosage_in_range("Digite a dosagem desejada entre 2-4mg/kg: ", 2, 4)
                dose = calculate_dose_mg(weight, dosage)
                print(f"Administrar {dose}mg VO em noites alternadas.")
                break
            print("Combinação inválida. Escolha espécie e caso novamente.")
    else:
        print("Princípio ativo inválido ou indisponível! Tente novamente.")


if __name__ == "__main__":
    run_cli()
