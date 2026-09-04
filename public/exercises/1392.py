# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero filtrando únicamente aquellos valores que sean mayores que cero (reemplazando los menores o iguales a cero por cero).
# difficulty: Intermedio
# expected_output: [[2, 0], [0, 5]]
# hint: Primero obtén las dimensiones de la matriz original, luego crea la transpuesta iterando sobre las columnas y filas, y aplica la condición para los valores <= 0.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear la matriz transpuesta con las dimensiones invertidas
    transpuesta = [[0] * filas for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            # Transpone y filtra: si es menor o igual a 0, se queda en 0
            transpuesta[j][i] = valor if valor > 0 else 0
            
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[2, -3], [0, 5]]) == [[2, 0], [-3, 5]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[-1, -2], [-3, -4]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")