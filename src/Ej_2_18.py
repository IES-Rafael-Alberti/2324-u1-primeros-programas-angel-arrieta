def nombreCompleto(nombreCompleto):
    nombreMinuscula = nombreCompleto.lower()
    nombreMayuscula = nombreCompleto.upper()
    nombrePrimeraMayuscula = nombreCompleto.title()
    return (nombreMinuscula, nombreMayuscula, nombrePrimeraMayuscula)


if __name__ == "__main__":
    mayuscula, minuscula, inicial = nombreCompleto(str(input("¿Cual es tu nombre completo?\n")))
    print(f"{minuscula}, {mayuscula}, {inicial}")