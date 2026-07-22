# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero filtrando únicamente aquellos valores que sean números pares.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Recuerda que para transponer una matriz puedes iterar sobre las columnas y luego sobre las filas, o usar listas por comprensión combinadas con zip(*matriz).

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    
    resultado = []
    for fila in transpuesta:
        pares_en_fila = [num for num in fila if num % 2 == 0]
        resultado.append(pares_en_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4]]) == [[2], [4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [], [3, 6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[5, 7], [9, 11]]) == [[], []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")