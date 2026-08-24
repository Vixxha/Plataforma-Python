# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes de tamaño N x M. La función debe primero transponer la matriz (intercambiar filas por columnas) y luego retornar una lista con el promedio aritmético de cada nueva fila (es decir, las columnas originales). Redondea cada promedio a 2 decimales.
# difficulty: Intermedio
# expected_output: [2.0, 3.0, 4.0]
# hint: Puedes usar list comprehensions o bucles anidados para acceder a los elementos por columnas antes de calcular el promedio. Recuerda usar round(valor, 2).

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    promedios = []
    for c in range(columnas):
        suma_columna = 0
        for f in range(filas):
            suma_columna += matriz[f][c]
        promedio = round(suma_columna / filas, 2)
        promedios.append(promedio)
        
    return promedios

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == [2.5, 3.5, 4.5], "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[10, 20], [30, 40], [50, 60]]) == [30.0, 40.0], "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[5]]) == [5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")