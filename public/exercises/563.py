# === METADATA ===
# title: Filtro y Promedio de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva lista plana que contenga solo los números mayores a 10, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [12, 15, 20, 25]
# hint: Puedes usar un bucle anidado o una lista por comprensión para aplanar la matriz, luego utiliza el método sort() o la función sorted().

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = [num for fila in matriz for num in fila if num > 10]
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 12, 8], [20, 3, 15], [25, 9, 1]]) == [12, 15, 20, 25], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[11, 10], [10, 11]]) == [11, 11], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")