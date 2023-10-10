def sumar(uno, dos, tres):
    return uno + dos + tres


if __name__ == "__main__":
    uno = float(input("Introduce un número: "))
    dos = float(input("Introduce otro número: "))
    tres = float(input("Introduce otro número más: "))
    print(f"El resultado da {sumar(uno, dos, tres)}")
