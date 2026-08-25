# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y devuelva una lista con la suma de los elementos de cada fila de esa nueva matriz transpuesta.
# difficulty: Intermedio
# expected_output: [12, 15, 18]
# hint: Recuerda que para obtener la transpuesta puedes recorrer las columnas usando índices o usar la compresión de listas junto con la función zip(*matriz).

# === SOLUTION ===
def transponer_y_sumar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Obtenemos la transpuesta usando zip
    transpuesta = [list(fila) for fila in zip(*matriz)]
    
    # Calculamos la suma de cada fila de la matriz transpuesta
    return [sum(fila) for fila in transpuesta]

# === TESTS ===
try:
    assert transponer_y_sumar([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9], "Error: el test 1 ha fallado."
    assert transponer_y_sumar([[1, 1], [1, 1]]) == [2, 2], "Error: considera casos límites en tu lógica."
    assert transponer_y_sumar([[10]]) == [10], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")