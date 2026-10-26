# === METADATA ===
# title: Operaciones Básicas en Matrices (Vectores de Vectores)
# description: Escribe una función que tome una matriz (lista de listas) cuadrada de números enteros y devuelva una lista con la suma de los elementos de cada columna.
# difficulty: Intermedio
# expected_output: [6, 15, 24]
# hint: Puedes recorrer la matriz usando índices o transponerla usando un bucle o comprensiones de lista.

# === SOLUTION ===
def sumar_columnas(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    
    for j in range(columnas):
        suma_col = 0
        for i in range(filas):
            suma_col += matriz[i][j]
        resultado.append(suma_col)
        
    return resultado

# === TESTS ===
try:
    assert sumar_columnas([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [12, 15, 18], "Error: el test 1 ha fallado."
    assert sumar_columnas([[1, 1], [1, 1]]) == [2, 2], "Error: considera casos límites en tu lógica."
    assert sumar_columnas([[10]]) == [10], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")