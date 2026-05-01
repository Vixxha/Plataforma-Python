# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una lista plana (vector) con todos los números mayores a 10, multiplicados por 2, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [22, 24, 26, 30]
# hint: Puedes usar una lista por comprensión para aplanar la matriz y filtrar los elementos simultáneamente, luego aplica el método sort().

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = [num * 2 for fila in matriz for num in fila if num > 10]
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 11], [13, 2], [15, 8]]) == [22, 26, 30], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [], "Error: debería devolver una lista vacía si no hay números > 10."
    assert procesar_matriz([[20, 10], [12, 5]]) == [24, 40], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")