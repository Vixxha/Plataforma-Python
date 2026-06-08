# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista que contenga únicamente aquellas filas cuya suma de elementos sea mayor o igual al promedio de la suma de todas las filas.
# difficulty: Intermedio
# expected_output: [[5, 6], [7, 8]] (para una entrada donde esas filas cumplen la condición)
# hint: Calcula primero la suma de cada fila, luego el promedio de esas sumas y finalmente filtra las filas originales.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio_global = sum(sumas) / len(sumas)
    
    resultado = [matriz[i] for i in range(len(matriz)) if sumas[i] >= promedio_global]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [3, 4], [5, 6]]) == [[3, 4], [5, 6]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[10, 10], [1, 1], [2, 2]]) == [[10, 10]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[5, 5]]) == [[5, 5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")