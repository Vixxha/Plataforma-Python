# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero filtrando únicamente aquellos valores que sean mayores que cero (reemplazando los menores o iguales a cero por cero).
# difficulty: Intermedio
# expected_output: [[1, 0, 5], [0, 3, 0]]
# hint: Primero crea la matriz transpuesta recorriendo los índices de columnas y filas, y luego aplica la condición para filtrar los valores menores o iguales a cero.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear la matriz transpuesta con ceros o directamente construyéndola
    transpuesta = []
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            # Filtrar valores <= 0
            if valor > 0:
                nueva_fila.append(valor)
            else:
                nueva_fila.append(0)
        transpuesta.append(nueva_fila)
        
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 3], [0, 5, -1]]) == [[1, 0], [-2, 5], [3, -1]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[0, 0], [0, 0]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")