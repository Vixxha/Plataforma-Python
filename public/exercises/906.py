# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos valores que sean números negativos, reemplazándolos por un cero.
# difficulty: Intermedio
# expected_output: [[1, 0, 7], [2, 5, 0], [0, 6, 9]]
# hint: Recuerda que para transponer una matriz puedes iterar sobre las columnas y luego sobre las filas, y puedes usar una condición para filtrar los números menores a cero.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_resultado = []
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            if valor < 0:
                nueva_fila.append(0)
            else:
                nueva_fila.append(valor)
        matriz_resultado.append(nueva_fila)
        
    return matriz_resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 3], [4, 5, -6]]) == [[1, 4], [0, 5], [3, 0]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[0, 1], [-5, 6]]) == [[0, 0], [1, 6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[-1, -2], [-3, -4]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")