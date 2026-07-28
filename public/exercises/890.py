# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego filtre cada fila resultante eliminando los números impares, dejando únicamente los números pares. Si una fila queda vacía, debe mantenerse como una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [6], []]
# hint: Puedes primero construir la transpuesta recorriendo los índices de las columnas y luego usar una comprensión de lista para filtrar los números pares de cada nueva fila.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta_filtrada = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            val = matriz[f][c]
            if val % 2 == 0:
                nueva_fila.append(val)
        transpuesta_filtrada.append(nueva_fila)
        
    return transpuesta_filtrada

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4], [5, 6]]) == [[2, 4], [6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[2, 4, 6]]) == [[2], [4], [6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")