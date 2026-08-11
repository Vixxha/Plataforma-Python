# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego filtre cada fila resultante para conservar únicamente los números pares. Si una fila queda vacía tras el filtrado, debe incluirse como una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [2], [6, 8]]
# hint: Puedes recorrer la matriz por columnas usando comprensiones de lista y la función zip(*matriz) para obtener la transpuesta fácilmente.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Obtener la matriz transpuesta
    transpuesta = [list(fila) for fila in zip(*matriz)]
    
    # Filtrar solo los números pares en cada fila de la transpuesta
    resultado = [[num for num in fila if num % 2 == 0] for fila in transpuesta]
    
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[2, 3, 4], [5, 6, 7]]) == [[2, 5], [3, 6], [4, 7]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")