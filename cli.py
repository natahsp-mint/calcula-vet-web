from services.calculator import calculate_dose_mg
from services.drug_service import get_drug_protocol

def run_cli():
    print("=== Calculadora Vet CLI ===")

    weight = float(input("Peso do animal (kg): "))
    drug = input("Princípio ativo: ").lower()

    protocol = get_drug_protocol(drug, weight)

    if protocol:
        print("\nResultado:")
        print(protocol)
    else:
        print("Fármaco não encontrado.")

if __name__ == "__main__":
    run_cli()
