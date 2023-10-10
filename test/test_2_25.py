from src.Ej_2_25 import fechado


def test_fechado():
    assert fechado("24/12/2003") == ("24", "diciembre", "2003")
