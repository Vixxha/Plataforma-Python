# === METADATA ===
# title: Filtrar y Trasponer Matriz Diagonal
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros. La función debe sumar los elementos que se encuentran en la diagonal principal y devolver una tupla que contenga: 1) Dicha suma, y 2) Una nueva matriz donde todos los elementos que no pertenezcan a la diagonal principal hayan sido reemplazados por ceros (0).
# difficulty: Intermedio
# expected_output: (15, [[1, 0, 0], [0, 5, 0], [0, 0, 9]])
# hint: Puedes recorrer la matriz usando dos bucles anidados (o por índices usando range) y verificar si el índice de la fila es igual al índice de la columna para identificar los elementos de la diagonal.

# === SOLUTION ===
def procesar_diagonal_matriz(matriz):
    n = len(matriz)
    suma_diagonal = 0
    # Crear una matriz de ceros del mismo tamaño
    matriz_resultado = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                suma_diagonal += matriz[i][j]
                matriz_resultado[i][j] = matriz[i][j]
                
    return (suma_diagonal, matriz_resultado)

# === TESTS ===
try:
    assert procesar_diagonal_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == (15, [[1, 0, 0], [0, 5, 0], [0, 0, 9]]), "Error: el test 1 ha fallado."
    assert procesar_diagonal_matriz([[4]]) == (4, [[4]]), "Error: considera casos límites en tu lógica."
    assert procesar_diagonal_matriz([[0, 2], [3, -5]]) == (-5, [[0, 0], [0, -5]]), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")