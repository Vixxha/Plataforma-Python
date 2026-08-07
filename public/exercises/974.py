# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes de tamaño N x M. La función debe retornar una tupla con dos elementos: primero, la matriz transpuesta (filas se vuelven columnas), y segundo, una lista con el promedio de cada columna de la matriz original.
# difficulty: Intermedio
# expected_output: (([[1, 4], [2, 5], [3, 6]], [2.0, 5.0, 8.0]) para la matriz [[1, 2, 3], [4, 5, 6]]
# hint: Puedes usar comprensión de listas para recorrer las columnas utilizando sus índices (ej. usando zip o rangos de tamaño).

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return [], []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Transponer la matriz
    matriz_transpuesta = [[matriz[f][c] for f in range(filas)] for c in range(columnas)]
    
    # Calcular el promedio de cada columna de la matriz original
    promedios_columnas = []
    for c in range(columnas):
        suma_columna = sum(matriz[f][c] for f in range(filas))
        promedios_columnas.append(suma_columna / filas)
        
    return matriz_transpuesta, promedios_columnas

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == ([[1, 4], [2, 5], [3, 6]], [2.5, 3.5, 4.5]), "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[10, 20], [30, 40], [50, 60]]) == ([[10, 30, 50], [20, 40, 60]], [30.0, 40.0]), "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[5]]) == ([[5]], [5.0]), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")