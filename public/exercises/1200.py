# === METADATA ===
# title: Transponer Matriz 2D
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones $N \times M$ y devuelva su matriz transposta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes utilizar listas por comprensión anidadas recorriendo los índices de las columnas y luego las filas, o usar un bucle tradicional.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_transpuesta = []
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            nueva_fila.append(matriz[f][c])
        matriz_transpuesta.append(nueva_fila)
        
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")