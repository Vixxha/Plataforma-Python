# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, calcule su matriz transpuesta (intercambiar filas por columnas) y luego filtre cada fila resultante para conservar únicamente los números pares. Si una fila queda vacía tras el filtrado, debe mantenerse como una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [6], [8]]
# hint: Puedes usar list comprehensions o bucles anidados para recorrer primero las columnas y luego las filas para obtener la transpuesta, y después aplicar otra comprensión para filtrar los pares.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = []
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            if valor % 2 == 0:
                nueva_fila.append(valor)
        transpuesta.append(nueva_fila)
        
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4]]) == [[2], [4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[4], [2, 5], [6]] or transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[4], [2], [6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[], []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")