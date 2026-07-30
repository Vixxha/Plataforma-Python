# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero filtrando únicamente aquellos valores que sean números pares.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Recuerda que para transponer una matriz puedes usar bucles anidados o comprensión de listas recorriendo las columnas primero y luego las filas.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            if valor % 2 == 0:
                nueva_fila.append(valor)
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4]]) == [[2], [4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[4], [2], [6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[], []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")