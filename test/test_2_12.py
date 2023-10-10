from src.Ej_2_12 import calculadora_imc


def test_calculadora_imc():
    assert calculadora_imc(90, 1.60) == 35.16
