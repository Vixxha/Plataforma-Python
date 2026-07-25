# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos valores que sean impares.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Recuerda que puedes usar list comprehensions o bucles anidados para acceder a los elementos por columna: matriz[j][i].

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    
    for j in range(columnas):
        fila_nueva = []
        for i in range(filas):
            valor = matriz[i][j]
            if valor % 2 == 0:
                fila_nueva.append(valor)
        resultado.append(fila_nueva)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2], [3, 4]]) == [[2], [4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[4], [2, 5], [6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")