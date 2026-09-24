# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero donde solo se incluyan aquellas columnas cuya suma total sea un número par. Si ninguna columna cumple la condición, retorna una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Primero transpón la matriz para trabajar con las columnas como filas, luego calcula la suma de cada una y filtra las que sean pares.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = [[matriz[r][c] for r in range(filas)] for c in range(columnas)]
    
    resultado = [col for col in transpuesta if sum(col) % 2 == 0]
    
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[2, 4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 1], [1, 1]]) == [[2, 2], [2, 2]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")