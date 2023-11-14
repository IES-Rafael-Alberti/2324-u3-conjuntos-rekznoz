from src.main5 import repetidos, pares, multipos_tres

def test_repetidos():
    c_primero = {1, 2, 3, 4}
    c_secundario = {3, 4, 5, 6}
    assert repetidos(c_primero, c_secundario) == {3, 4}

def test_pares():
    assert pares([2, 4, 6, 8, 5, 9 ,1]) == {2, 4, 6, 8}

def test_multipos_tres():
    assert multipos_tres([2, 4, 3, 6, 9, 12]) == {3, 6, 9, 12}