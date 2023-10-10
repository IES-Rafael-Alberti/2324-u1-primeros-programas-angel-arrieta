def cociente(n, m):
    return n//m


def resto(n, m):
    return n % m


if __name__ == "__main__":
    uno = int(input("Dime un dividendo: "))
    otro = int(input("Dime un divisor: "))
    print(f"la división de {uno} entre {otro} da un cociente {cociente(uno, otro)} y un resto {resto(uno, otro)}")
