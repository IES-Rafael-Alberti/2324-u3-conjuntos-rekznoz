from src.main1 import compras_domicilios

def test_viviendass():
    compras = [
        ("cliente1", "producto1", 100, "domicilio1"),
        ("cliente2", "producto2", 200, "domicilio2"),
        ("cliente1", "producto3", 150, "domicilio3")
    ]
    assert compras_domicilios(compras) == {"domicilio1", "domicilio2", "domicilio3"}
    compras = []
    assert compras_domicilios(compras) == set()