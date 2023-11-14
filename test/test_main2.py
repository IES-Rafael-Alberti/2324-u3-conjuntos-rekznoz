from src.main2 import control_bucle

def test_control_bucle():
    assert control_bucle("abc") == True
    assert control_bucle("123") == True
    assert control_bucle("x") == False
    assert control_bucle("special characters") == True