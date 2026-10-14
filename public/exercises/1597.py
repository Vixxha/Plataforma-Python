# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz que contenga únicamente las filas donde la suma de sus elementos sea un número par. Además, a esta matriz resultante se le debe aplicar la operación de transposición (intercambiar filas por columnas). Si ninguna fila cumple la condición, debe retornar una matriz vacía [].
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Primero recorre cada fila de la matriz para calcular su suma y filtrar las que sean pares. Luego, puedes usar comprensiones de listas anidadas o zip para calcular la transpuesta de la matriz resultante.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    if not matriz:
        return []
    
    filas_pares = [fila for fila in matriz if sum(fila) % 2 == 0]
    
    if not filas_pares:
        return []
        
    return [[filas_pares[i][j] for i in range(len(filas_pares))] for j in range(len(filas_pares[0]))]

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2], [3, 3]]) == [[2, 3]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[1, 1], [2, 2], [3, 5]]) == [[2], [2]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")