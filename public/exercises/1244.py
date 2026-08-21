# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero donde solo se incluyan aquellas columnas cuya suma total de elementos sea mayor o igual a 10. Si ninguna columna cumple la condición, retorna una lista vacía.
# difficulty: Intermedio
# expected_output: [[12, 15], [3, 4], [6, 8]]
# hint: Primero obtén la matriz transpuesta recorriendo las columnas originales, luego evalúa la suma de cada nueva fila (columna original) antes de añadirla al resultado final.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            nueva_fila.append(matriz[f][c])
        if sum(nueva_fila) >= 10:
            transpuesta.append(nueva_fila)
            
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[12, 15, 18]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 1], [1, 1]]) == [], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[5, 1, 3], [5, 2, 3]]) == [[10, 3, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")