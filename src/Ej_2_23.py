def cambio_dominio(correo):
    direccion = correo.split('@', 1)[0]
    nuevo_correo = direccion + "@ceu.es"
    return nuevo_correo


if __name__ == "__main__":
    print(cambio_dominio(str(input("Introduzca su correo:\n"))))
