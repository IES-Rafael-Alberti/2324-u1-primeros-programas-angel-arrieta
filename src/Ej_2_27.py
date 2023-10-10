def calculadora_producto(precio, cantidad):
    return precio * cantidad


if __name__ == "__main__":
    producto = input("Producto a comprar: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    compra_final = calculadora_producto(precio, cantidad)
    print(f"{producto} vale {precio:09.2f}\n"
    f"{cantidad:03d} {producto} vale {compra_final:011.2f}")
