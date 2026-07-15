# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una lista con las filas cuya suma de elementos sea mayor que el promedio de las sumas de todas las filas de la matriz.
# difficulty: Intermedio
# expected_output: [[7, 8, 9], [4, 5, 6]] (ejemplo según entrada)
# hint: Calcula primero la suma de cada fila, almacénalas en una lista auxiliar, obtén el promedio de esas sumas y luego filtra las filas originales.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio_total = sum(sumas) / len(sumas)
    
    resultado = [matriz[i] for i in range(len(matriz)) if sumas[i] > promedio_total]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [3, 4], [5, 6]]) == [[5, 6]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[10, 10], [1, 1], [5, 5]]) == [[10, 10]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")