def contar(nombre):
    return len(nombre)


if __name__ == "__main__":
    print(f"Tiene {contar(str(input('¿Cúal es tu nombre? ')))} letras")
