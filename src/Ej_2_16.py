def barras_pasadas(cantidad):
    return round((3.49 * 0.6 * cantidad), 2)


if __name__ == "__main__":
    barras_de_ayer = int(input("Introduce las barras vendidad que no son del día: "))
    print (f"Cada barra se vende a 3.49 euros, sí no es fresca se le descuenta un 60½\n"
    f"Se ha conseguido {barras_pasadas(barras_de_ayer)} euros de barras que no son del día")
