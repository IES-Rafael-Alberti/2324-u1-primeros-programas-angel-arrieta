from src.Ej_2_26 import lista_compra


def test_lista_compra():
    assert lista_compra("cuaderno, mochila, folios") == "cuaderno\n mochila\n folios"
