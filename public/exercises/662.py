# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista que contenga únicamente aquellas filas cuya suma de elementos sea mayor o igual al promedio de la suma de todas las filas.
# difficulty: Intermedio
# expected_output: [[5, 5], [9, 1]]
# hint: Calcula primero la suma de cada fila, luego obtén el promedio global de esas sumas y utiliza una estructura de filtrado para seleccionar las filas correspondientes.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas_filas = [sum(fila) for fila in matriz]
    promedio_global = sum(sumas_filas) / len(sumas_filas)
    
    resultado = [matriz[i] for i in range(len(matriz)) if sumas_filas[i] >= promedio_global]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[5, 5], [1, 2], [9, 1]]) == [[5, 5], [9, 1]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1]]) == [[1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[10], [0], [5]]) == [[10], [5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")