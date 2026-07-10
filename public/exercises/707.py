# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista que contenga únicamente aquellas filas cuya suma de elementos sea mayor o igual que el promedio de las sumas de todas las filas.
# difficulty: Intermedio
# expected_output: [[7, 8], [9, 10]]
# hint: Primero calcula la suma de cada fila, luego obtén el promedio global de esas sumas y finalmente filtra la matriz original comparando.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio_sumas = sum(sumas) / len(sumas)
    
    resultado = [matriz[i] for i in range(len(matriz)) if sumas[i] >= promedio_sumas]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [7, 8], [9, 10]]) == [[7, 8], [9, 10]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1], [1, 1]]) == [[1, 1], [1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[10], [1], [2]]) == [[10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")