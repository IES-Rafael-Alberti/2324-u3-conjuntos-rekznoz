from src.main6 import juntar

def test_repetidos():
    c_primero = {1, 2, 3, 4}
    c_secundario = {3, 4, 5, 6}
    assert juntar(c_primero, c_secundario) == {1, 2, 3, 4, 5, 6}