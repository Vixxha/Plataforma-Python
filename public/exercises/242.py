# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos hayan sido reemplazados por 0.
# difficulty: Intermedio
# expected_output: [[1, 0, 3], [0, 5, 0]] para la entrada [[1, -2, 3], [-4, 5, -6]]
# hint: Utiliza un bucle anidado o una lista de comprensión para iterar sobre cada fila y cada elemento de la matriz.

# === SOLUTION ===
def normalizar_matriz(matriz):
    resultado = []
    for fila in matriz:
        nueva_fila = [x if x >= 0 else 0 for x in fila]
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert normalizar_matriz([[1, -2, 3], [-4, 5, -6]]) == [[1, 0, 3], [0, 5, 0]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[-1, -1], [-1, -1]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([[0, 1], [2, 3]]) == [[0, 1], [2, 3]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")