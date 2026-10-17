# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros. La función debe primero eliminar todas las filas donde la suma de sus elementos sea un número par. Luego, de las filas restantes, debe retornar la matriz traspuesta (intercambiar filas por columnas). Si no quedan filas, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5]]
# hint: Puedes usar list comprehensions o bucles para calcular la suma de cada fila antes de filtrar, y luego usar zip(*matriz_filtrada) para calcular la traspuesta de manera eficiente.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    if not matriz:
        return []
    
    # Filtrar filas cuya suma sea impar
    filas_filtradas = [fila for fila in matriz if sum(fila) % 2 != 0]
    
    if not filas_filtradas:
        return []
    
    # Calcular la traspuesta de las filas filtradas
    # Usamos zip para transponer
    traspuesta = [list(columna) for columna in zip(*filas_filtradas)]
    
    return traspuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[2, 4], [6, 8]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 1, 1], [2, 2, 2], [3, 1, 1]]) == [[1, 3], [1, 1], [1, 1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")