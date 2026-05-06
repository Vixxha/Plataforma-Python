# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde solo se conserven los números pares, sustituyendo los impares por 0, y finalmente devuelva la matriz transpuesta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[2, 0], [0, 4]] para la entrada [[2, 0], [1, 4]]
# hint: Primero recorre la matriz para aplicar la lógica de los pares (usando el operador módulo %), luego utiliza comprensión de listas o bucles anidados para intercambiar los índices i, j por j, i.

# === SOLUTION ===
def procesar_matriz(matriz):
    filas = len(matriz)
    cols = len(matriz[0])
    
    # Paso 1: Filtrar pares
    filtrada = [[(val if val % 2 == 0 else 0) for val in fila] for fila in matriz]
    
    # Paso 2: Transponer
    transpuesta = [[filtrada[i][j] for i in range(filas)] for j in range(cols)]
    
    return transpuesta

# === TESTS ===
try:
    assert procesar_matriz([[1, 2], [3, 4]]) == [[0, 0], [2, 4]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, 5], [7, 8], [2, 1]]) == [[0, 8, 2], [10, 0, 0]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[1, 1], [1, 1]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")