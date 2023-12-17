# Funció Iterativa para suma de los primeros n números naturales

def suma_naturales_iterativa(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Ejemplo de uso
n = 5
resultado = suma_naturales_iterativa(n)
print(f"La suma de los primeros {n} números naturales es: {resultado}")

#Versión Recursiva

def suma_naturales_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales_recursiva(n - 1)

# Ejemplo de uso
n = 5
resultado = suma_naturales_recursiva(n)
print(f"La suma de los primeros {n} números naturales es: {resultado}")
