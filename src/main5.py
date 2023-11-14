
def repetidos(c_primero, c_secundario):
    return c_primero & c_secundario

def pares(lista):
    numeros = set()
    for numero in  lista:
        if numero % 2 == 0:
            numeros.add(numero)
    return numeros

def multipos_tres(lista): 
    numeros = set()
    for numero in lista:
        if numero % 3 == 0:
            numeros.add(numero)
    return numeros

if __name__ == "__main__":

    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    par = pares(numeros)
    
    mutiplos_3 = multipos_tres(numeros)
    pares_multiplos = repetidos(par, mutiplos_3)

    print(par)
    print(mutiplos_3)
    print(pares_multiplos)