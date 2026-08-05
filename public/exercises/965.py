# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero filtrando únicamente aquellos valores que sean números pares.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Recuerda que para transponer una matriz puedes iterar sobre las columnas y luego sobre las filas, o usar comprensión de listas anidadas evaluando la condición de número par.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    
    for c in range(columnas):
        fila_nueva = []
        for f in range(filas):
            val = matriz[f][c]
            if val % 2 == 0:
                fila_nueva.append(val)
        resultado.append(fila_nueva)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4]]) == [[2], [4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[4], [2], [6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[], []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")