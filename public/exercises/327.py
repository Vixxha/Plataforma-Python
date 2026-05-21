# === METADATA ===
# title: Filtro y Promedio de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista con el promedio de cada fila, pero excluyendo todos los números negativos de cada cálculo. Si una fila solo contiene números negativos o está vacía, el promedio debe ser 0.
# difficulty: Intermedio
# expected_output: [2.5, 5.0, 0] para la entrada [[1, 4, -2], [5, 5], [-1, -5]]
# hint: Utiliza list comprehensions o bucles anidados para filtrar los valores positivos antes de calcular la media. Recuerda validar la división por cero.

# === SOLUTION ===
def promedio_filas_positivas(matriz):
    resultados = []
    for fila in matriz:
        positivos = [num for num in fila if num > 0]
        if not positivos:
            resultados.append(0.0)
        else:
            promedio = sum(positivos) / len(positivos)
            resultados.append(float(promedio))
    return resultados

# === TESTS ===
try:
    assert promedio_filas_positivas([[1, 4, -2], [5, 5], [-1, -5]]) == [2.5, 5.0, 0.0], "Error: el test 1 ha fallado."
    assert promedio_filas_positivas([[10, 20], [0, 0], [100]]) == [15.0, 0.0, 100.0], "Error: considera casos límites en tu lógica."
    assert promedio_filas_positivas([[], [-1]]) == [0.0, 0.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")