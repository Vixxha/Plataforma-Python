# === METADATA ===
# title: Filtrado de matriz y suma diagonal
# description: Crea una función que reciba una matriz cuadrada (lista de listas) de números enteros y devuelva una lista con dos elementos: primero, la suma de los elementos que se encuentran en la diagonal principal, y segundo, una nueva lista con todos los números de la matriz que sean mayores a un valor umbral dado.
# difficulty: Intermedio
# expected_output: [15, [7, 8, 9, 6]]
# hint: Utiliza un bucle anidado para recorrer la matriz y el índice [i][i] para acceder a la diagonal principal.

# === SOLUTION ===
def procesar_matriz(matriz, umbral):
    suma_diagonal = 0
    filtrados = []
    
    for i in range(len(matriz)):
        suma_diagonal += matriz[i][i]
        for j in range(len(matriz[i])):
            if matriz[i][j] > umbral:
                filtrados.append(matriz[i][j])
                
    return [suma_diagonal, filtrados]

# === TESTS ===
try:
    assert procesar_matriz([[1, 2], [3, 4]], 2) == [5, [3, 4]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[5, 0, 0], [0, 5, 0], [0, 0, 5]], 2) == [15, [5, 5, 5]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[1, 1], [1, 1]], 5) == [2, []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")