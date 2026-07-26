# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego devuelva una lista con la suma de los elementos de cada columna de la matriz original (que corresponden a las filas de la transpuesta).
# difficulty: Intermedio
# expected_output: [15, 18, 21]
# hint: Puedes recorrer la matriz usando bucles anidados o comprensiones de lista para acceder a los elementos por columnas usando sus índices.

# === SOLUTION ===
def transponer_y_sumar_columnas(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    sumas = []
    
    for c in range(columnas):
        suma_columna = 0
        for f in range(filas):
            suma_columna += matriz[f][c]
        sumas.append(suma_columna)
        
    return sumas

# === TESTS ===
try:
    assert transponer_y_sumar_columnas([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [12, 15, 18], "Error: el test 1 ha fallado."
    assert transponer_y_sumar_columnas([[10, 20], [30, 40], [50, 60]]) == [90, 120], "Error: considera casos límites en tu lógica."
    assert transponer_y_sumar_columnas([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")