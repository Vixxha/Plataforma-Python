# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva lista que contenga únicamente las filas cuya suma total sea mayor al promedio de la suma de todas las filas.
# difficulty: Intermedio
# expected_output: [[10, 20], [30, 40]]
# hint: Primero calcula la suma de cada fila, luego obtén el promedio de esos resultados y finalmente filtra las filas originales comparando cada suma individual contra ese promedio.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio_total = sum(sumas) / len(sumas)
    
    resultado = [fila for i, fila in enumerate(matriz) if sumas[i] > promedio_total]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [10, 20], [30, 40]]) == [[10, 20], [30, 40]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[5, 5], [1, 1], [2, 2]]) == [[5, 5]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")