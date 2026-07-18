# === METADATA ===
# title: Transformación de Matriz en Vector
# description: Escribe una función que tome una matriz (lista de listas) de números enteros y devuelva una lista única (vector) que contenga todos los elementos de la matriz, pero solo aquellos que sean números pares, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [2, 4, 6, 8]
# hint: Puedes iterar sobre cada fila de la matriz y luego sobre cada elemento, o utilizar una comprensión de listas para filtrar los números pares antes de ordenarlos.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento % 2 == 0:
                resultado.append(elemento)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[1, 2], [3, 4]]) == [2, 4], "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, 5, 8], [6, 1, 3]]) == [6, 8, 10], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[1, 3, 5], [7, 9]]) == [], "Error: el caso base (sin pares) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")