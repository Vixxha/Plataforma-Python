# === METADATA ===
# title: Filtrar y Multiplicar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y un número escalar. La función debe retornar una nueva matriz donde solo se mantengan aquellos números que son mayores a 0, y cada uno de estos elementos debe ser multiplicado por el valor del escalar. Si una fila queda vacía tras el filtrado, debe descartarse o mantenerse vacía según corresponda al resultado de la operación por fila.
# difficulty: Intermedio
# expected_output: [[-1, 2], [3, 4]] con escalar 2 -> [[4], [6, 8]]
# hint: Puedes usar listas por comprensión anidadas para recorrer las filas y columnas de la matriz eficientemente aplicando las dos condiciones (filtrado y multiplicación).

# === SOLUTION ===
def procesar_matriz(matriz, escalar):
    resultado = []
    for fila in matriz:
        fila_filtrada = [x * escalar for x in fila if x > 0]
        if fila_filtrada:
            resultado.append(fila_filtrada)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[-1, 2], [3, -5, 4]], 2) == [[4], [6, 8]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[0, -2, -5], [-1, -3]], 3) == [], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[1, 2], [3, 4]], 10) == [[10, 20], [30, 40]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")