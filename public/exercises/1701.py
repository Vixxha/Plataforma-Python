# === METADATA ===
# title: Filtrar y Rotar Matriz Cuadrada
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros y un número entero `k`. La función debe eliminar todas las filas cuya suma de elementos sea un número impar y, posteriormente, rotar la matriz resultante 90 grados en sentido horario. Si la matriz queda vacía después de filtrar, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [[3, 1], [4, 2]]
# hint: Primero calcula la suma de cada fila para filtrar las impares. Luego, recuerda que rotar 90 grados en sentido horario una matriz equivale a transponerla y luego invertir cada una de sus filas.

# === SOLUTION ===
def filtrar_y_rotar_matriz(matriz, k):
    if not matriz or not matriz[0]:
        return []
    
    # Filtrar filas cuya suma sea par
    matriz_filtrada = [fila for fila in matriz if sum(fila) % 2 == 0]
    
    if not matriz_filtrada:
        return []
    
    # Rotar la matriz 90 grados en sentido horario (transponer y revertir filas)
    filas = len(matriz_filtrada)
    columnas = len(matriz_filtrada[0])
    
    transpuesta = [[matriz_filtrada[r][c] for r in range(filas)] for c in range(columnas)]
    matriz_rotada = [fila[::-1] for fila in transpuesta]
    
    return matriz_rotada

# === TESTS ===
try:
    assert filtrar_y_rotar_matriz([[1, 2], [3, 4]], 1) == [[3, 1], [4, 2]], "Error: el test 1 ha fallado."
    assert filtrar_y_rotar_matriz([[1, 1], [1, 1]], 2) == [[1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_rotar_matriz([[1, 3], [5, 7]], 1) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")