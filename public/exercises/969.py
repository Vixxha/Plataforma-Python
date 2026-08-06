# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes de tamaño N x M. La función debe primero transponer la matriz (intercambiar filas por columnas) y luego retornar una nueva lista con el promedio de los valores de cada fila de la matriz transpuesta. El resultado debe ser redondeado a 2 decimales.
# difficulty: Intermedio
# expected_output: [2.0, 3.5]
# hint: Recuerda que la transpuesta de una matriz intercambia las coordenadas [i][j] por [j][i]. Puedes usar listas por comprensión para recorrer las columnas.

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Transponer la matriz
    transpuesta = [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
    
    # Calcular el promedio de cada fila de la transpuesta
    promedios = [round(sum(fila) / len(fila), 2) for fila in transpuesta]
    
    return promedios

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2], [3, 4]]) == [2.0, 3.0], "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == [2.5, 3.5, 4.5], "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[10]]) == [10.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")