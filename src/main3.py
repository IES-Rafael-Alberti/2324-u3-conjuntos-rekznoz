
def conjunto_potencia(s):

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