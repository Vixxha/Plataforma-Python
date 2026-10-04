# === METADATA ===
# title: Matriz de Caloría Cero
# description: Dada una matriz (lista de listas) de números enteros que representan lecturas de sensores, implementa una función que devuelva una nueva matriz donde cualquier fila o columna que contenga al menos un cero sea completamente reemplazada por ceros.
# difficulty: Intermedio
# expected_output: [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
# hint: Primero identifica los índices de las filas y columnas que contienen al menos un cero, antes de modificar la matriz para evitar propagaciones erróneas.

# === SOLUTION ===
def matriz_cero(matriz):
    if not matriz or not matriz[0]:
        return matriz
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    filas_cero = set()
    cols_cero = set()
    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 0:
                filas_cero.add(i)
                cols_cero.add(j)
                
    resultado = [[matriz[i][j] for j in range(columnas)] for i in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            if i in filas_cero or j in cols_cero:
                resultado[i][j] = 0
                
    return resultado

# === TESTS ===
try:
    assert matriz_cero([[1, 2, 3], [4, 0, 6], [7, 8, 9]]) == [[1, 0, 3], [0, 0, 0], [7, 0, 9]], "Error: el test 1 ha fallado."
    assert matriz_cero([[0, 2], [3, 4]]) == [[0, 0], [0, 4]], "Error: considera casos límites en tu lógica."
    assert matriz_cero([[1, 1], [1, 1]]) == [[1, 1], [1, 1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")