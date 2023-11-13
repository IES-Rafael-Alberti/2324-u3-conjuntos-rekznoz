
def compras_domicilios(ListaClientes):
    Direccion = set()
    for i in ListaClientes:
        Direccion.add(i[3])
    return Direccion

if __name__ == "__main__":

    compras = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
        ("Jorge Russo", 7, 699, "Mirasol 218"), 
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    domicilios_facturacion = compras_domicilios(compras)
    print(domicilios_facturacion)
