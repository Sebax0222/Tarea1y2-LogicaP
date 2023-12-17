#Funcion que suma todos los elementos de una lista de manera iterativa.

def suma_lista_iterativa(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
resultado = suma_lista_iterativa(mi_lista)
print(resultado)


#Forma Recursiva

def suma_lista_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista_recursiva(lista[1:])

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
resultado = suma_lista_recursiva(mi_lista)
print(resultado)
