# === METADATA ===
# title: Filtro de Valores en Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un umbral. La función debe retornar una nueva lista plana que contenga solo los elementos de la matriz que sean mayores o iguales al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [10, 15, 20]
# hint: Puedes iterar sobre cada fila de la matriz y luego sobre cada elemento, o usar una comprensión de listas anidada para aplanar y filtrar al mismo tiempo.

# === SOLUTION ===
def filtrar_y_ordenar_matriz(matriz, umbral):
    resultado = [num for fila in matriz for num in fila if num >= umbral]
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_ordenar_matriz([[5, 10], [1, 20], [15, 3]], 10) == [10, 15, 20], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[1, 2], [3, 4]], 5) == [], "Error: considera casos donde ningún elemento cumple el criterio."
    assert filtrar_y_ordenar_matriz([[0, 0], [0, 0]], 0) == [0, 0, 0, 0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")