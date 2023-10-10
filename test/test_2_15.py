from src.Ej_2_15 import intereses


def test_intereses():
    assert intereses(100) == (104.0, 108.16, 112.49)
