# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean negativos (reemplazándolos por 0). Asume que la matriz de entrada es rectangular.
# difficulty: Intermedio
# expected_output: [[1, 0, 5], [2, 4, 0]]
# hint: Puedes recorrer las columnas primero y luego las filas para lograr la transposición, y usar una condición para filtrar los números menores a cero.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            nueva_fila.append(valor if valor >= 0 else 0)
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 5], [2, 4, -3]]) == [[1, 2], [0, 4], [5, 0]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[0, 0], [0, 0]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[-5]]) == [[0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")