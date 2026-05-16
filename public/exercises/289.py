# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista que contenga únicamente aquellas filas cuya suma de elementos sea mayor o igual al promedio de la suma de todas las filas.
# difficulty: Intermedio
# expected_output: [[10, 20], [5, 5, 5, 5]]
# hint: Primero calcula la suma de cada fila y almacénalas en una lista auxiliar, luego calcula el promedio de esas sumas para realizar el filtrado.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio = sum(sumas) / len(sumas)
    
    resultado = [matriz[i] for i in range(len(matriz)) if sumas[i] >= promedio]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [10, 20], [5, 5, 5, 5]]) == [[10, 20], [5, 5, 5, 5]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1], [1, 1]]) == [[1, 1], [1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[100], [1], [1]]) == [[100]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")