
def juntar(c_primero, c_secundario):
    return c_primero | c_secundario

if __name__ == '__main__':
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    letras_comunes = juntar(vocales, consonantes)
    ordenado = sorted(letras_comunes)
    print(ordenado)