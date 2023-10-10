from src.Ej_2_5 import calcular_iva


def test_calcular_iva():
    assert calcular_iva(50, 21) == 60.5
