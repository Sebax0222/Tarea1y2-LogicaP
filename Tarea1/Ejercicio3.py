# Funcion que realiza conteo regresivo desde un número dado hasta 1.

def conteo_regresivo(numero):
    for i in range(numero, 0, -1):
        print(i)

# Ejemplo de uso
numero_inicial = 5
conteo_regresivo(numero_inicial)

#Forma recursiva

def conteo_regresivo_recursivo(numero):
    if numero <= 0:
        return
    else:
        print(numero)
        conteo_regresivo_recursivo(numero - 1)

# Ejemplo de uso
numero_inicial = 5
conteo_regresivo_recursivo(numero_inicial)
