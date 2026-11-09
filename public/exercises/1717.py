# === METADATA ===
# title: Transponer Matriz
# description: Escribe una función que reciba una matriz (lista de listas) representada como un vector bidimensional de dimensiones $N \times M$ y devuelva su matriz transpuesta ($M \times N$). La transpuesta de una matriz se obtiene intercambiando sus filas por columnas.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes utilizar listas de comprensión anidadas o recorrer la matriz utilizando los índices de columnas y filas invertidos (es decir, matriz[j][i]).

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Construimos la matriz transpuesta usando comprensión de listas
    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")