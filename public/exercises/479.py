# === METADATA ===
# title: Filtrado de matriz y promedio de filas
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista donde cada elemento es el promedio de los números positivos encontrados en cada fila. Si una fila no tiene números positivos, el promedio debe ser 0.0.
# difficulty: Intermedio
# expected_output: [5.0, 0.0, 7.5] para la matriz [[2, 8, -1], [-5, -2], [10, 5]]
# hint: Recorre cada sublista, filtra los elementos mayores a cero y asegúrate de no dividir por cero al calcular el promedio.

# === SOLUTION ===
def promedio_positivos(matriz):
    resultados = []
    for fila in matriz:
        positivos = [num for num in fila if num > 0]
        if not positivos:
            resultados.append(0.0)
        else:
            resultados.append(sum(positivos) / len(positivos))
    return resultados

# === TESTS ===
try:
    assert promedio_positivos([[2, 8, -1], [-5, -2], [10, 5]]) == [5.0, 0.0, 7.5], "Error: el test 1 ha fallado."
    assert promedio_positivos([[0, 0], [1, 2, 3]]) == [0.0, 2.0], "Error: considera casos límites en tu lógica."
    assert promedio_positivos([[]]) == [0.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")