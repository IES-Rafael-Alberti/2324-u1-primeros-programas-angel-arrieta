def suman(uno, dos):
    return uno + dos


if __name__ == "__main__":
    uno = float(input("Introduce un número: "))
    dos = float(input("Introduce otro número: "))
    uno = suman(uno, dos)
    dos = float(input("Introduce otro número más: "))
    print(suman(uno, dos))
