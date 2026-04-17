import unicodedata

input = lambda prompt="": __import__("builtins").input(prompt).replace(",", ".")

#fix in case numeric value is asked and user mistakes the entry
def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Resposta inválida! Tente novamente.")

#fix in case user types value out of given range
def get_dosage_in_range(prompt, min_value, max_value):
    while True:
        dosage = get_numeric_input(prompt)
        if min_value <= dosage <= max_value:
            return dosage
        print(f"Valor fora da faixa permitida ({min_value}-{max_value} mg/kg).")


print("Bem-vindo ao Calcula Vet Web!")
print("A calculadora baseada no Guia Terapêutico Veterinário 4ª Edição.")
# ask for the drug name and store it in a variable (retry if invalid)
VALID_DRUGS = (
    "amoxicilina",
    "dipirona",
    "doxiciclina",
    "enrofloxacina",
    "enrofloxacino",
    "maropitant",
    "maropitante",
    "meloxicam",
    "metronidazol",
    "omeprazol",
    "prednisolona"
)
while True:
    drug = input("Digite o nome do princípio ativo: ")
    drug = drug.lower()
    drug = "".join(char for char in unicodedata.normalize("NFD", drug) if unicodedata.category(char) != "Mn")
    if drug in VALID_DRUGS:
        break
    print("Princípio ativo inválido ou indisponível! Tente novamente.")
dose = 1.0
# asks for the weight of the animal and store it in a variable
weight = get_numeric_input("Digite o peso do animal: ")

# the user types amoxicilina
if drug == "amoxicilina":
    dosage = get_dosage_in_range("Digite a dosagem desejada entre 10-20mg/kg: ", 10, 20)
    dose = dosage * weight
    print(f"Administrar {dose}mg IM/SC/VO a cada 8-12 horas.")

# the user types dipirona
elif drug == "dipirona":
    dose = 25 * weight
    print(f"Administrar {dose}mg IV/IM/SC/VO a cada 8 horas.")

# the user types doxiciclina
elif drug == "doxiciclina":
    dose = 10 * weight
    print(f"Administrar {dose}mg IV/VO a cada 12-24 horas.")

# the user types enrofloxacina / enrofloxacino 
elif drug in ("enrofloxacina", "enrofloxacino"):
    print("1 - Cão")
    print("2 - Gato")
    while True:
        species = input("Selecione a opção da espécie: ")
        if species == "1":
            dosage = get_dosage_in_range("Digite a dosagem desejada entre 5-10mg/kg: ", 5, 10)
            dose = dosage * weight
            print(f"Administrar {dose}mg IM/VO a cada 12-24 horas.")
            break
        elif species == "2":
            dose = 2.5 * weight
            print(f"Administrar {dose}mg VO a cada 12 horas.")
            break
        print("Opção inválida. Escolha 1 (Cão) ou 2 (Gato).")

# the user types maropitant
if drug in ("maropitant", "maropitante"):
    print(f"Administrar {weight}mg SC/VO SID")

# the user types meloxicam
elif drug == "meloxicam":
    print("1 - Cão")
    print("2 - Gato")
    while True:
        species = input("Selecione a opção da espécie: ")
        if species == "1":
            dose = 0.1 * weight
            print(f"Iniciar com {0.2 * weight}mg IV/SC/VO, continuando com {dose}mg VO SID.")
            break
        elif species == "2":
            dose = 0.05 * weight
            print(f"Iniciar com {0.1 * weight}mg SC/VO, continuando com {dose}mg VO SID. Pode também ser usada uma dose única de {0.3 * weight}mg.")
            break
        print("Opção inválida. Escolha 1 (Cão) ou 2 (Gato).")

# the user types metronidazol
if drug == "metronidazol":
    print("1 - Giardíase")
    print("2 - Anaeróbicos")
    while True:
        case = input("Digite a opção desejada: ")
        if case == "1":
            dose = 25 * weight
            print(f"Administrar {dose}mg BID ou {2*dose}mg SID VO por 5 dias.")
            break
        elif case == "2":
            dose = 15 * weight
            print(f"Administrar {dose}mg IV/VO BID.")
            break
        print("Opção inválida. Escolha 1 ou 2.")

# the user types omeprazol
if drug == "omeprazol":
    dosage = get_dosage_in_range("Digite a dosagem desejada entre 0.5-1mg/kg: ", 0.5, 1)
    dose = dosage * weight
    print(f"Administrar {dose}mg VO SID.")

# the user types prednisolona
if drug == "prednisolona":
    print("1 - Cão")
    print("2 - Gato")
    species = input("Selecione a opção da espécie: ")
    print("1 - Alergia")
    print("2 - Imunossupressão")
    print("3 - Uso prolongado")
    case = input("Digite a opção desejada: ")
    while True:
        if species == "1" and case == "1":
            dosage = get_dosage_in_range("Digite a dosagem desejada entre 0.5-1mg/kg: ", 0.5, 1)
            dose = dosage * weight
            print(f"Administrar {dose}mg IM/VO BID.")
            break
        elif species == "1" and case == "2":
            dose = 2 * weight
            print(f"Administrar {dose}mg IM/VO BID.")
            break
        elif species == "1" and case == "3":
            dosage = get_dosage_in_range("Digite a dosagem desejada entre 0.5-2mg/kg: ", 0.5, 2)
            dose = dosage * weight
            print(f"Administrar {dose}mg VO em manhãs alternadas.")
            break
        elif species == "2" and case == "1":
            dose = 1 * weight
            print(f"Administrar {dose}mg IM/VO BID.")
            break
        elif species == "2" and case == "2":
            dose = 3 * weight
            print(f"Administrar {dose}mg IM/VO BID.")
            break
        elif species == "2" and case == "3":
            dosage = get_dosage_in_range("Digite a dosagem desejada entre 2-4mg/kg: ", 2, 4)
            dose = dosage * weight
            print(f"Administrar {dose}mg VO em noites alternadas.")
            break
        print("Opção inválida.")
