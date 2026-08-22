# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero donde cada elemento haya sido multiplicado por 2 si es un número par, o dejado intacto si es impar.
# difficulty: Intermedio
# expected_output: [[2, 6], [4, 8]]
# hint: Primero puedes crear la matriz transpuesta iterando sobre las columnas originales y luego aplicar la condición de multiplicación a cada elemento.

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
            val = matriz[f][c]
            if val % 2 == 0:
                nueva_fila.append(val * 2)
            else:
                nueva_fila.append(val)
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[2, 6], [4, 8]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 1], [1, 1]]) == [[1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[2, 4, 6]]) == [[4], [8], [12]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")