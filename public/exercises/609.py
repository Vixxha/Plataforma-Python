# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos sean reemplazados por 0, y todos los valores positivos sean multiplicados por 2.
# difficulty: Intermedio
# expected_output: [[0, 4, 6], [0, 10, 0]]
# hint: Utiliza bucles anidados para recorrer las filas y columnas, o aprovecha la comprensión de listas para crear la nueva estructura.

# === SOLUTION ===
def procesar_matriz(matriz):
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for valor in fila:
            if valor < 0:
                nueva_fila.append(0)
            else:
                nueva_fila.append(valor * 2)
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

# === TESTS ===
try:
    assert procesar_matriz([[-1, 2, 3], [-5, 5, 0]]) == [[0, 4, 6], [0, 10, 0]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, -10], [20, -20]]) == [[20, 0], [40, 0]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[]]) == [[]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")