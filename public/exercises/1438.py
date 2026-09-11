# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego devuelva una lista con la suma de los elementos de cada fila de esa nueva matriz transpuesta.
# difficulty: Intermedio
# expected_output: [15, 18, 21]
# hint: Recuerda que la transposición de una matriz implica que el elemento en la posición [i][j] pasa a estar en [j][i]. Puedes iterar por columnas o usar comprensión de listas.

# === SOLUTION ===
def transponer_y_sumar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Construir la transpuesta y sumar sus filas al mismo tiempo
    resultado = []
    for c in range(columnas):
        suma_columna = 0
        for f in range(filas):
            suma_columna += matriz[f][c]
        resultado.append(suma_columna)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_sumar([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9], "Error: el test 1 ha fallado."
    assert transponer_y_sumar([[1, 1], [1, 1]]) == [2, 2], "Error: considera casos límites en tu lógica."
    assert transponer_y_sumar([[10]]) == [10], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")