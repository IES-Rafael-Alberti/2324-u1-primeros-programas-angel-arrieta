def sustraer_iva(precio_final):
    return round(precio_final / 110 * 100, 2)


if __name__ == "__main__":
    precio = float(input("Dime el precio final del producto (IVA 10% aplicado): "))
    print(f"El precio inicial es {sustraer_iva(precio)}")
