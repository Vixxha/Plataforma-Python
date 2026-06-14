# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista que contenga solo aquellas filas cuyo promedio de elementos sea estrictamente mayor que un valor umbral dado.
# difficulty: Intermedio
# expected_output: [[10, 20], [30, 40]]
# hint: Calcula el promedio de cada sublista sumando sus elementos y dividiéndolos por la cantidad de elementos (len), luego compara con el umbral.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz, umbral):
    resultado = []
    for fila in matriz:
        if len(fila) > 0:
            promedio = sum(fila) / len(fila)
            if promedio > umbral:
                resultado.append(fila)
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [10, 20], [30, 40]], 15) == [[10, 20], [30, 40]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[5, 5], [1, 1], [0, 0]], 2) == [[5, 5]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[10]], 5) == [[10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")