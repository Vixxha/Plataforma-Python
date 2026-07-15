# === METADATA ===
# title: Filtrado de matriz y promedio de filas
# description: Crea una función que reciba una matriz (lista de listas) de números enteros, filtre los valores menores a 0 reemplazándolos por 0 y retorne una lista con el promedio de cada fila resultante.
# difficulty: Intermedio
# expected_output: [2.0, 5.0]
# hint: Utiliza bucles anidados o comprensión de listas para procesar cada elemento y la función sum() para calcular el promedio.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultados = []
    for fila in matriz:
        fila_filtrada = [max(0, x) for x in fila]
        promedio = sum(fila_filtrada) / len(fila_filtrada) if len(fila_filtrada) > 0 else 0
        resultados.append(float(promedio))
    return resultados

# === TESTS ===
try:
    assert procesar_matriz([[1, 3, 2], [-5, 10, 0]]) == [2.0, 3.3333333333333335], "Error: el test 1 ha fallado."
    assert procesar_matriz([[-1, -1], [4, 4]]) == [0.0, 4.0], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[10], [20]]) == [10.0, 20.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")