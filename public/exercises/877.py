# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes de tamaño N x M. La función debe primero transponer la matriz (intercambiar filas por columnas) y luego retornar una nueva lista con el promedio de los valores de cada fila de la matriz transpuesta. El resultado debe redondearse a 2 decimales.
# difficulty: Intermedio
# expected_output: [2.5, 3.5]
# hint: Puedes recorrer la matriz usando bucles anidados o comprensión de listas para acceder a los elementos por columna (transposición) antes de calcular el promedio.

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Transponer la matriz
    matriz_transpuesta = [[matriz[f][c] for f in range(filas)] for c in range(columnas)]
    
    # Calcular el promedio de cada fila de la transpuesta
    promedios = [round(sum(fila) / len(fila), 2) for fila in matriz_transpuesta]
    
    return promedios

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2], [3, 4]]) == [2.0, 3.0], "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == [2.5, 3.5, 4.5], "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[10]]) == [10.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")