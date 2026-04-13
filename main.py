print("Bem-vindo ao Calcula Vet Web!")
print("A calculadora baseada no Guia Terapêutico Veterinário 4ª Edição.")
# ask for the drug name and store it in a variable (retry if invalid)
VALID_DRUGS = (
    "amoxicilina",
    "dipirona",
    "doxiciclina",
    "enrofloxacina",
    "enrofloxacino",
    "meloxicam",
)
while True:
    drug = input("Digite o nome do princípio ativo (sem letras maiúsculas e sem acento): ")
    if drug in VALID_DRUGS:
        break
    print("Princípio ativo inválido ou ainda indisponível. Digite outro.")
dose = 1.0
# ask for the weight of the animal and store it in a variable
weight = float(input("Digite o peso do animal: "))
# the user types amoxicilina
if drug == "amoxicilina":
    dosage = float(input("Qual dosagem desejada entre 10-20mg/kg (digite apenas o número):"))
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
# the user types enrofloxacina / enrofloxacino (same cálculo)
elif drug in ("enrofloxacina", "enrofloxacino"):
    print("1 - Cão")
    print("2 - Gato")
    while True:
        species = input("Selecione a espécie (digite apenas o número): ")
        if species == "1":
            dosage = float(input("Qual dosagem desejada entre 5-10mg/kg (digite apenas o número):"))
            dose = dosage * weight
            print(f"Administrar {dose}mg IM/VO a cada 12-24 horas.")
            break
        elif species == "2":
            dose = 2.5 * weight
            print(f"Administrar {dose}mg VO a cada 12 horas.")
            break
        print("Opção inválida. Escolha 1 (Cão) ou 2 (Gato).")
# the user types maropitant
# the user types meloxicam
elif drug == "meloxicam":
    print("1 - Cão")
    print("2 - Gato")
    while True:
        species = input("Selecione a espécie (digite apenas o número): ")
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
# the user types omeprazol
# the user types prednisolona