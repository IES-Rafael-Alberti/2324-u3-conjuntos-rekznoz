
def control_bucle(entrada):
    if entrada == "x":
        return False
    else:
        return True

if __name__ == "__main__":

    nombres_primaria = set()
    nombres_secundaria = set()
    nombre = ""

    print("Ingresa nombres de alumnos en primaria ('x' para finalizar)")

    while control_bucle(nombre):
        nombre = input("> ")
        if control_bucle(nombre):
            nombres_primaria.add(nombre)

    nombre = ""
    print("Ingresa nombres de alumnos en secundaria ('x' para finalizar)")
    while control_bucle(nombre):
        nombre = input("> ")
        if control_bucle(nombre):
            nombres_secundaria.add(nombre)

    todos = nombres_primaria.union(nombres_secundaria)
    print("Todos los nombres")
    print(todos)

    repetidos = nombres_primaria.intersection(nombres_secundaria)
    print("Nombres repetidos en primaria y secundaria")
    print(repetidos)

    no_repetidos_secundaria = nombres_primaria.difference(nombres_secundaria)
    print("Nombres de primaria que no se repiten en secundaria")
    print(no_repetidos_secundaria)

    todos_secundaria = nombres_primaria.issubset(nombres_secundaria)
    print("¿ Estan todos los nombres de primaria en secundaria ? True o False")
    print(todos_secundaria)
