# === METADATA ===
# title: Filtrado de Matriz y Suma Diagonal
# description: Crea una función que reciba una matriz cuadrada (lista de listas) de números enteros y devuelva una lista con dos elementos: primero, la suma de los elementos de la diagonal principal, y segundo, una lista filtrada que contenga únicamente los números pares encontrados en toda la matriz (en orden de aparición).
# difficulty: Intermedio
# expected_output: [15, [2, 4, 6, 8]]
# hint: Usa dos ciclos anidados para recorrer la matriz. Para la diagonal principal, recuerda que los elementos cumplen la condición donde el índice de la fila es igual al índice de la columna.

# === SOLUTION ===
def procesar_matriz(matriz):
    suma_diagonal = 0
    pares = []
    n = len(matriz)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                suma_diagonal += matriz[i][j]
            if matriz[i][j] % 2 == 0:
                pares.append(matriz[i][j])
                
    return [suma_diagonal, pares]

# === TESTS ===
try:
    assert procesar_matriz([[1, 2], [3, 4]]) == [5, [2, 4]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[5, 0, 1], [2, 6, 3], [4, 8, 7]]) == [18, [0, 2, 6, 4, 8]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[10]]) == [10, [10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")