from src.main3 import conjunto_potencia
import pytest

def test_conjunto_potencia():

    conjunto = {1, 2, 3}

    resultado = conjunto_potencia(conjunto)

    assert len(resultado) == 8
    assert set() in resultado
    assert {1} in resultado
    assert {2} in resultado
    assert {3} in resultado
    assert {1, 2} in resultado
    assert {1, 3} in resultado
    assert {2, 3} in resultado
    assert conjunto in resultado