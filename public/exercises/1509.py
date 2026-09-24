# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean negativos (reemplazándolos por 0). Asume que la matriz de entrada es rectangular.
# difficulty: Intermedio
# expected_output: [[1, 0, 3], [0, 5, 0]]
# hint: Puedes primero recorrer la matriz original para reemplazar los negativos por 0, o hacerlo durante el proceso de transposición creando listas para cada nueva columna.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear matriz transpuesta de dimensiones invertidas
    resultado = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            # Si el valor es negativo, se convierte en 0
            if valor < 0:
                resultado[j][i] = 0
            else:
                resultado[j][i] = valor
                
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 3], [-4, 5, -6]]) == [[1, 0], [0, 5], [3, 0]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[0, 2], [3, 4]]) == [[0, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[-1, -1], [-1, -1]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")