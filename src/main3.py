
def conjunto_potencia(s):
    """
    Genera el conjunto de partes de un conjunto dado.

    Argumentos:
        s (conjunto): El conjunto de entrada para el cual se necesita generar el conjunto de partes.

    return:
        potencia (lista): El conjunto de partes del conjunto de entrada s. Cada elemento en el conjunto de partes es un conjunto que representa un subconjunto de s.

    """
    potencia = [set()]
    
    for elemento in s:
        nuevos_subconjuntos = []
        for subconjunto in potencia:
            nuevos_subconjuntos.append(subconjunto.union({elemento}))
        potencia.extend(nuevos_subconjuntos)
    
    return potencia

if __name__ == "__main__":

    conjunto = {6, 1, 4}
    resultado = conjunto_potencia(conjunto)
    print(resultado)