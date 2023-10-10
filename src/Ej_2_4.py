def conv_a_Fahrenheit(celsius):
    return celsius * 1.8 + 32


if __name__ == "__main__":
    celsius = float(input("Dime una temperatura en ºC: "))
    print(f"{celsius}ºC son {conv_a_Fahrenheit(celsius)}ºF")
