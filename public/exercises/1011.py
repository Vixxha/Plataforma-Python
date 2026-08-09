# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz (transpuesta) donde las filas se convierten en columnas, pero filtrando previamente o posteriormente para que solo queden aquellos números que sean pares. Nota: Si una fila o columna queda vacía después de filtrar, se mantiene. Sin embargo, para este ejercicio, aplica el filtro de pares a toda la matriz resultante de la transposición o viceversa: devuelve una matriz con las mismas dimensiones donde los impares se reemplazan por 0, o simplemente filtra los elementos pares. Más exactamente: transpón la matriz y luego devuelve una matriz donde todos los elementos impares hayan sido reemplazados por el número 0.
# difficulty: Intermedio
# expected_output: [[2, 0], [0, 4]]
# hint: Recuerda que la transposición de una matriz intercambia sus filas por columnas ($matriz[j][i]$). Puedes recorrer la matriz por columnas y luego por filas, evaluando si cada número es par.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear matriz transpuesta con ceros o construida directamente
    transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            val = matriz[i][j]
            # Transponer y mantener solo pares (si es impar, queda en 0 por defecto)
            if val % 2 == 0:
                transpuesta[j][i] = val
                
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4]]) == [[0, 0], [2, 4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[5, 6, 7], [8, 9, 10]]) == [[0, 8], [6, 0], [0, 10]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")