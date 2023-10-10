def calculadora_imc(peso, estatura):
    return round(peso / estatura**2, 2)


if __name__ == "__maim__":
    peso = float(input("Introduce tu peso en kilogramos: "))
    estatura = float(input("Introduce tu estaura en metros: "))
    print(f"Tú índice de masa corporal es {calculadora_imc(peso, estatura)}")
