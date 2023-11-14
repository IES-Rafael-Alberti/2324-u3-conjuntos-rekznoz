
def repetidos(c_primero, c_secundario):

    return c_primero & c_secundario

def no_repetidos(c_primero, c_secundario):
    
    return c_primero - c_secundario

if __name__ == "__main__":

    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)

    frutas_comunes = repetidos(set_frutas1, set_frutas2)

    frutas_solo_en_frutas1 = no_repetidos(set_frutas1, set_frutas2)

    frutas_solo_en_frutas2 = no_repetidos(set_frutas2, set_frutas1)

    print("Frutas comunes ", frutas_comunes)
    print("Frutas solo en frutas1 ", frutas_solo_en_frutas1)
    print("Frutas solo en frutas2 ", frutas_solo_en_frutas2)
