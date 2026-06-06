# === METADATA ===
# title: Filtrado de Matriz y Suma Diagonal
# description: Crea una función que reciba una matriz cuadrada (lista de listas) de números enteros y devuelva una lista con dos elementos: primero, la suma de los elementos de la diagonal principal, y segundo, el valor máximo encontrado en toda la matriz.
# difficulty: Intermedio
# expected_output: [15, 9] (Para una matriz 3x3 donde la diagonal suma 15 y el mayor elemento es 9)
# hint: Puedes usar un bucle anidado para recorrer toda la matriz y, cuando el índice de fila sea igual al de columna, estarás en la diagonal principal.

# === SOLUTION ===
def procesar_matriz(matriz):
    n = len(matriz)
    suma_diagonal = 0
    valor_maximo = matriz[0][0]
    
    for i in range(n):
        for j in range(n):
            # Sumar si es diagonal
            if i == j:
                suma_diagonal += matriz[i][j]
            # Actualizar máximo
            if matriz[i][j] > valor_maximo:
                valor_maximo = matriz[i][j]
                
    return [suma_diagonal, valor_maximo]

# === TESTS ===
try:
    assert procesar_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [15, 9], "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, 0], [0, 5]]) == [15, 10], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[7]]) == [7, 7], "Error: el caso base de matriz 1x1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")