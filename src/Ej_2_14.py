def peso_paquete(payasos, munecas):
    return (payasos * 112 + munecas * 75) / 100


if __name__ == "__main__":
    peso = peso_paquete(int(input("Introduce los payasos del pedido: ")),int(input("Introduce las muñecas del pedido: ")))
    print(f"El paquete pesa {peso} kilogramos")
