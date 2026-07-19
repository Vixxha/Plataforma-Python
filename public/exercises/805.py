# === METADATA ===
# title: Filtrado de Matriz y Promedio
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista con el promedio de cada fila, pero excluyendo todos los números negativos de cada cálculo. Si una fila solo contiene negativos, el promedio debe ser 0.
# difficulty: Intermedio
# expected_output: [2.5, 4.0, 0.0]
# hint: Recorre cada fila, utiliza una lista temporal para filtrar los números positivos y luego calcula el promedio evitando la división por cero.

# === SOLUTION ===
def promedio_filas_sin_negativos(matriz):
    resultados = []
    for fila in matriz:
        positivos = [num for num in fila if num >= 0]
        if not positivos:
            resultados.append(0.0)
        else:
            resultados.append(sum(positivos) / len(positivos))
    return resultados

# === TESTS ===
try:
    assert promedio_filas_sin_negativos([[1, 4, -2], [2, 6], [-1, -5]]) == [2.5, 4.0, 0.0], "Error: el test 1 ha fallado."
    assert promedio_filas_sin_negativos([[10, 20], [0, 0], [-10]]) == [15.0, 0.0, 0.0], "Error: considera casos límites en tu lógica."
    assert promedio_filas_sin_negativos([[], [5]]) == [0.0, 5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")