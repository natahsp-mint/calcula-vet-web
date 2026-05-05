def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Valor inválido, tente novamente.")
