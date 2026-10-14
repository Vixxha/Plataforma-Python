# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego filtre cada fila resultante eliminando los números que sean menores o iguales a cero.
# difficulty: Intermedio
# expected_output: [[2, 5], [1, 6], [3]]
# hint: Puedes usar la comprensión de listas para recorrer las columnas y construir la transpuesta, y luego aplicar otra comprensión para filtrar los elementos mayores a cero.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta_filtrada = []
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            if valor > 0:
                nueva_fila.append(valor)
        transpuesta_filtrada.append(nueva_fila)
        
    return transpuesta_filtrada

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 3], [4, 5, -6]]) == [[1, 4], [], [3]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[-1, 2], [3, -4], [5, 6]]) == [[3, 5], [2, 6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[0, 0], [0, 0]]) == [[], []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")