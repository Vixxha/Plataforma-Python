# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes de dimensiones $N \times M$. La función debe primero transponer la matriz (intercambiar filas por columnas) y luego retornar una nueva lista con el promedio aritmético de cada una de las filas de la matriz transpuesta. Redondea cada promedio a 2 decimales.
# difficulty: Intermedio
# expected_output: [2.5, 3.5]
# hint: Recuerda que puedes acceder a las columnas de una matriz iterando por sus índices o utilizando compresión de listas junto con la función zip (*matriz).

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Transponemos la matriz usando zip
    transpuesta = list(zip(*matriz))
    
    # Calculamos el promedio de cada fila transpuesta y redondeamos a 2 decimales
    promedios = [round(sum(fila) / len(fila), 2) for fila in transpuesta]
    
    return promedios

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == [2.5, 3.5, 4.5], "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[10, 20], [30, 40], [50, 60]]) == [30.0, 40.0], "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[5]]) == [5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")