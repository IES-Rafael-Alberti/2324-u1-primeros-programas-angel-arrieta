def desglose(precio):
    unidades = round(precio, 2)//1
    return int(unidades), int((precio-unidades)*100)


if __name__ == "__main__":
    unidades, centimos = desglose(float(input("Introduzca el precio de un producto: ")))
    print(f"El artículo vale {unidades} euros y {centimos} centimos")
