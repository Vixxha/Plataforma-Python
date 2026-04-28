# === METADATA ===
# title: Filtrado de Matriz de Adyacencia
# description: Dada una matriz (lista de listas) que representa una cuadrícula de números, escribe una función que devuelva una lista plana con todos los elementos que sean mayores que un umbral dado y que además sean números pares.
# difficulty: Intermedio
# expected_output: [4, 6, 8]
# hint: Puedes usar un bucle anidado para recorrer las filas y columnas, o utilizar una comprensión de lista (list comprehension) para filtrar los elementos.

# === SOLUTION ===
def filtrar_matriz(matriz, umbral):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > umbral and elemento % 2 == 0:
                resultado.append(elemento)
    return resultado

# === TESTS ===
try:
    assert filtrar_matriz([[1, 4, 3], [6, 2, 8]], 3) == [4, 6, 8], "Error: el test 1 ha fallado."
    assert filtrar_matriz([[1, 2], [3, 4]], 5) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_matriz([[10, 11], [12, 13]], 9) == [10, 12], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")