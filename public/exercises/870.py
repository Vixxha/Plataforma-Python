# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero donde solo se incluyan aquellas columnas cuya suma total de elementos sea mayor o igual a 10. Si ninguna columna cumple la condición, retorna una lista vacía.
# difficulty: Intermedio
# expected_output: [[6, 6], [7, 5], [8, 4]]
# hint: Primero calcula la transposta de la matriz iterando sobre los índices de columnas y filas. Luego, filtra las columnas basándote en la suma de sus elementos.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta_filtrada = []
    
    for c in range(columnas):
        columna_actual = [matriz[f][c] for f in range(filas)]
        if sum(columna_actual) >= 10:
            transpuesta_filtrada.append(columna_actual)
            
    return transpuesta_filtrada

# === TESTS ===
try:
    matriz_test_1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    # Columnas originales: 
    # Col 0: [1, 4] suma = 5 (< 10)
    # Col 1: [2, 5] suma = 7 (< 10)
    # Col 2: [3, 6] suma = 9 (< 10)
    # Resultado esperado: []
    assert transponer_y_filtrar(matriz_test_1) == [], "Error: el test 1 ha fallado."

    matriz_test_2 = [
        [1, 2, 3],
        [5, 5, 5]
    ]
    # Columnas originales:
    # Col 0: [1, 5] suma = 6 (< 10)
    # Col 1: [2, 5] suma = 7 (< 10)
    # Col 2: [3, 5] suma = 8 (< 10)
    # Espere, hagamos una con sumas >= 10:
    # [ [1, 2, 3], [9, 5, 5] ] -> Col 0: [1,9]=10, Col 1: [2,5]=7, Col 2: [3,5]=8
    # Usemos otra matriz para el test 2:
    matriz_test_2_real = [
        [1, 2, 3],
        [9, 4, 5]
    ]
    # Col 0: [1, 9] = 10 ( >= 10 ) -> Transpuesta: [1, 9]
    # Col 1: [2, 4] = 6  ( < 10 )
    # Col 2: [3, 5] = 8  ( < 10 )
    assert transponer_y_filtrar(matriz_test_2_real) == [[1, 9]], "Error: considera casos límites en tu lógica."

    matriz_test_3 = [
        [1, 2, 3],
        [5, 5, 5],
        [2, 3, 1]
    ]
    # Matriz 3x3:
    # Col 0: [1, 5, 2] = 8 (< 10)
    # Col 1: [2, 5, 3] = 10 (>= 10) -> [2, 5, 3]
    # Col 2: [3, 5, 1] = 9 (< 10)
    assert transponer_y_filtrar(matriz_test_3) == [[2, 5, 3]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")