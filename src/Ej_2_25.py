def fechado(fecha):
    dia = fecha[:-8]
    mes = (int(fecha[:-5][-2:])) - 1
    ano = fecha[-4:]
    lista_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                "noviembre", "diciembre"]
    mes_escrito = lista_meses[mes]
    return dia, mes_escrito, ano


if __name__ == "__main__":
    dia, mes_escrito, ano = fechado(str(input("Introduzca su fecha de nacimiento (formato dd/mm/aaaa)\n")))
    print(f"Usted nacio el {dia} de {mes_escrito} del año {ano}")
