# Funcion Iterativa para calcular potencia de un número

def calcular_potencia(base, exponente):
    resultado = 1

    for _ in range(exponente):
        resultado *= base

    return resultado

# Ejemplo de uso
base = 2
exponente = 3
resultado = calcular_potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

#Versión recursiva

def calcular_potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia_recursiva(base, exponente - 1)

# Ejemplo de uso
base = 2
exponente = 3
resultado = calcular_potencia_recursiva(base, exponente)
print(f"{base}^{exponente} = {resultado}")

