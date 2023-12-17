import bisect

class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __lt__(self, other):
        return self.nombre < other.nombre

personas = [
    Persona("Alice", 25, 160),
    Persona("Bob", 30, 175),
    Persona("Charlie", 22, 170),
    Persona("David", 28, 180),
    Persona("Eva", 35, 165)
]

personas.sort()

def buscar_persona_por_nombre(lista, nombre):
    index = bisect.bisect_left(lista, Persona(nombre, 0, 0))
    if index != len(lista) and lista[index].nombre == nombre:
        return lista[index]
    else:
        return None

# Ejemplo de uso 
nombre_a_buscar = "David"
persona_encontrada = buscar_persona_por_nombre(personas, nombre_a_buscar)

if persona_encontrada:
    print(f"Persona encontrada: {persona_encontrada.nombre}, Edad: {persona_encontrada.edad}, Altura: {persona_encontrada.altura}")
else:
    print(f"No se encontró a ninguna persona con el nombre {nombre_a_buscar}.")
