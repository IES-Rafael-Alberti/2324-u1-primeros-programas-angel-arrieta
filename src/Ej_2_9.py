def sumar(uno, dos, tres):
    return uno + dos + tres


if __name__ == "__main__":
    numero = sumar(float(input("Introduce un número: ")), float(input("Otro: ")), float(input("Otro más: ")))
    print(f"El resultado da {numero}")