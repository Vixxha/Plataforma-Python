# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero donde solo se incluyan aquellas columnas cuya suma total sea mayor o igual a un valor umbral dado.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero calcula la matriz transpuesta y luego evalúa la suma de cada nueva fila antes de decidir si incluirla en el resultado final.

# === SOLUTION ===
def transponer_y_filtrar(matriz, umbral):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = []
    for c in range(columnas):
        nueva_fila = [matriz[f][c] for f in range(filas)]
        if sum(nueva_fila) >= umbral:
            transpuesta.append(nueva_fila)
            
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]], 10) == [[3], [6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 2], [3, 4]], 5) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 1], [1, 1]], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")