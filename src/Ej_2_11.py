def sumatorio(num):
    return num * (num +1) / 2


if __name__ == "__maim__":
    numero = float(input("Introduce un número para hacer\t su sumatorio (1 + 2 + 3 +...+ n): "))
    print(f"El sumatorio de {numero} es {sumatorio(numero)}")
