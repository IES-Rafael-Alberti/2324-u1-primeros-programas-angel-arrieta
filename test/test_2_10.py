from src.Ej_2_10 import operacion


def test_operacion():
    assert operacion() == ((3 + 2) / (2 * 5)) ** 2
