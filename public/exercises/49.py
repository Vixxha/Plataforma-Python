# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una nueva lista que contenga solo los números mayores a 10, multiplicados por 2, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [22, 24, 30]
# hint: Puedes usar una lista de comprensión para aplanar la matriz y filtrar los elementos simultáneamente antes de ordenarlos.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento * 2)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 12], [8, 15], [3, 11]]) == [22, 24, 30], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[20, 10], [5, 30]]) == [40, 60], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")