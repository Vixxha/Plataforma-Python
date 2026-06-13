# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos sean reemplazados por 0, y todos los valores positivos sean normalizados restándoles el valor mínimo de la matriz original.
# difficulty: Intermedio
# expected_output: [[0, 2, 0], [1, 0, 4]]
# hint: Primero encuentra el valor mínimo de toda la matriz, luego utiliza bucles anidados o una comprensión de listas para transformar los elementos.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not matriz[0]:
        return matriz
    
    todos_los_valores = [val for fila in matriz for val in fila]
    min_val = min(todos_los_valores)
    
    resultado = []
    for fila in matriz:
        nueva_fila = []
        for val in fila:
            if val < 0:
                nueva_fila.append(0)
            else:
                nueva_fila.append(val - min_val)
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 7, 2], [6, 2, 9]]) == [[3, 5, 0], [4, 0, 7]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[-1, 2], [-5, 0]]) == [[0, 3], [0, 1]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[10, 10], [10, 10]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")