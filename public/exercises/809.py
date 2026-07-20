# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos se conviertan en 0 y todos los valores positivos se mantengan igual.
# difficulty: Intermedio
# expected_output: [[1, 0, 3], [0, 5, 0]]
# hint: Puedes usar bucles anidados para recorrer cada fila y cada columna, o utilizar comprensión de listas para una solución más compacta.

# === SOLUTION ===
def normalizar_matriz(matriz):
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = [valor if valor > 0 else 0 for valor in fila]
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

# === TESTS ===
try:
    assert normalizar_matriz([[1, -2, 3], [-4, 5, -6]]) == [[1, 0, 3], [0, 5, 0]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[0, 0], [0, 0]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([[-1, -1], [1, 1]]) == [[0, 0], [1, 1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")