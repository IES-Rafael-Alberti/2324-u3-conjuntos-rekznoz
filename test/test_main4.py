from src.main4 import repetidos, no_repetidos

def test_repetidos():
    c_primero = {1, 2, 3, 4}
    c_secundario = {3, 4, 5, 6}
    assert repetidos(c_primero, c_secundario) == {3, 4}

def test_no_repetidos():
    c_primero = {1, 2, 3}
    c_secundario = {4, 5, 6}
    assert no_repetidos(c_primero, c_secundario) == {1, 2, 3}