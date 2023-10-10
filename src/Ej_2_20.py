def telefono(numero):
    return numero[3:12]


if __name__ == "__main__":
    telefono_formateado = telefono((str(input("Introduzca un número en formato prefijo-número-extension [+XX-(9X)-XX]\n"))))
    print(f"El número original es {telefono_formateado}")
