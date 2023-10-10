def calcular_iva(articulo, impuesto):
    return articulo + articulo / 100 * impuesto


if __name__ == "__main__":
    articulo = float(input("Dime el precio del producto: "))
    impuesto = float(input("Dime el impuesto a añadir: "))
    print(f"El precio con IVA es {calcular_iva(articulo, impuesto)}")