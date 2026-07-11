# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros, filtre solo aquellos elementos que son pares y devuelva una nueva matriz (lista de listas) donde cada fila original se convierta en una columna (trasposición), manteniendo solo los valores pares. Si un valor es impar, debe ser omitido en la estructura resultante.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]] si la entrada es [[1, 2], [3, 4], [5, 6], [7, 8]]
# hint: Primero filtra los pares de cada sublista, luego usa zip(*lista) para trasponer la estructura resultante de forma eficiente.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    filtrada = [[num for num in fila if num % 2 == 0] for fila in matriz]
    # Filtramos filas vacías resultantes para asegurar una trasposición consistente
    filtrada = [fila for fila in filtrada if fila]
    return [list(columna) for columna in zip(*filtrada)]

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[2, 4, 6, 8]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[10, 11], [12, 13]]) == [[10], [12]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 3], [5, 7]]) == [], "Error: el caso base falló (debe devolver lista vacía si no hay pares)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")