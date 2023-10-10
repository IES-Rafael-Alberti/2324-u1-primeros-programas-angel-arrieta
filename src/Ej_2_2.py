def importe(hora, coste):
    return hora * coste


if __name__ == "__main__":
    horas = int(input("Horas de trabajo: "))
    coste = int(input("Coste por hora: "))
    print(f"Importe total: {importe(horas, coste)}")
