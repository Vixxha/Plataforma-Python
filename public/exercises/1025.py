# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean negativos (reemplazándolos por 0). Asume que la matriz de entrada es rectangular.
# difficulty: Intermedio
# expected_output: [[1, 0, 5], [0, 4, 6]] para la entrada [[1, -2], [3, 4], [-5, 6]]
# hint: Puedes recorrer la matriz original usando sus índices de filas y columnas, creando primero la estructura transpuesta y aplicando la condición de filtrado.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear la matriz transpuesta con ceros
    transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            # Si es negativo se convierte en 0, de lo contrario se mantiene
            transpuesta[j][i] = valor if valor >= 0 else 0
            
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2], [3, 4], [-5, 6]]) == [[1, 3, 0], [0, 4, 6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[-1, -1], [-1, -1]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")