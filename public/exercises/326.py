# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una nueva lista conteniendo únicamente aquellas filas cuya suma de elementos sea mayor que el promedio de la suma de todas las filas.
# difficulty: Intermedio
# expected_output: [[5, 5], [10, 2]]
# hint: Primero calcula la suma de cada fila, luego obtén el promedio global de esas sumas y finalmente filtra las filas que cumplan la condición.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio_total = sum(sumas) / len(sumas)
    
    return [matriz[i] for i in range(len(matriz)) if sumas[i] > promedio_total]

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [5, 5], [10, 2]]) == [[5, 5], [10, 2]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1]]) == [], "Error: considera casos donde ninguna fila supera el promedio."
    assert filtrar_filas_por_promedio([[10], [20], [30]]) == [[20], [30]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")