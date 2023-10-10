def intereses(balance):
    primer_ano = balance * 1.04
    segundo_ano = primer_ano * 1.04
    tercer_ano = segundo_ano * 1.04
    return round(primer_ano, 2), round(segundo_ano, 2), round(tercer_ano, 2)


if __name__ == "__main__":
    balance_inicial = float(input("Introduce el balance de tu cuenta\n(Interés ofrecido del 4%): "))
    primer_ano, segundo_ano, tercer_ano = intereses(balance_inicial)
    print(f"El primer año acabas con {primer_ano} euros\n"
            f"El segundo año acabas con {segundo_ano} euros\n"
            f"El tercer año acabas con {tercer_ano} euros")
