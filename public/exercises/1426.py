# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes, calcule su transpuesta (intercambiar filas por columnas) y luego devuelva una lista con el promedio de cada fila de la matriz transpuesta. Redondea cada promedio a 2 decimales.
# difficulty: Intermedio
# expected_output: [2.5, 3.5, 4.5]
# hint: Puedes recorrer la matriz usando bucles anidados o comprensiones de lista para obtener las columnas, y luego calcular el promedio de cada una.

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
    
    promedios = [round(sum(fila) / len(fila), 2) for fila in transpuesta]
    
    return promedios

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == [2.5, 3.5, 4.5], "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[10, 20], [30, 40], [50, 60]]) == [30.0, 40.0], "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[5]]) == [5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")