# === METADATA ===
# title: Analizador de Matriz de Adyacencia
# description: Crea una función que reciba una matriz cuadrada (lista de listas) que representa las conexiones de una red y devuelva una lista con el número de conexiones (sumatoria) de cada nodo.
# difficulty: Intermedio
# expected_output: [2, 1, 3] para una matriz de 3x3
# hint: Debes iterar sobre cada fila de la matriz y sumar sus elementos. Recuerda que la suma de los valores en una fila representa el grado del nodo.

# === SOLUTION ===
def calcular_grados_nodos(matriz):
    grados = []
    for fila in matriz:
        grados.append(sum(fila))
    return grados

# === TESTS ===
try:
    assert calcular_grados_nodos([[0, 1, 1], [1, 0, 0], [1, 1, 1]]) == [2, 1, 3], "Error: el test 1 ha fallado."
    assert calcular_grados_nodos([[0, 0], [0, 0]]) == [0, 0], "Error: considera casos límites en tu lógica."
    assert calcular_grados_nodos([[1, 1], [1, 1]]) == [2, 2], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")