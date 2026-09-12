# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego retorne una lista unidimensional con todos los elementos de la transpuesta que sean números pares, ordenados de menor a mayor.
# difficulty: Intermedio
# expected_output: [2, 4, 6, 8]
# hint: Primero obtén las dimensiones de la matriz para construir la transpuesta recorriendo las columnas como nuevas filas. Luego, extrae los pares, aplana la estructura y ordénala.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Construir la transpuesta
    transpuesta = [[matriz[f][c] for f in range(filas)] for c in range(columnas)]
    
    # Aplanar y filtrar pares
    pares = []
    for fila in transpuesta:
        for val in fila:
            if val % 2 == 0:
                pares.append(val)
                
    return sorted(pares)

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [2, 4, 6], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [], "Error: considera casos límites en tu lógica (sin pares)."
    assert transponer_y_filtrar_pares([[2, 8], [4, 6]]) == [2, 4, 6, 8], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")