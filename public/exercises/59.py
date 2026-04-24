# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una nueva lista conteniendo únicamente aquellas filas cuya suma sea mayor o igual que el promedio de las sumas de todas las filas.
# difficulty: Intermedio
# expected_output: [[10, 20], [5, 5, 5]]
# hint: Primero calcula la suma de cada fila y almacénalas en una lista auxiliar para luego calcular el promedio general.

# === SOLUTION ===
def filtrar_filas_por_promedio(matriz):
    if not matriz:
        return []
    
    sumas = [sum(fila) for fila in matriz]
    promedio_general = sum(sumas) / len(sumas)
    
    resultado = [matriz[i] for i in range(len(matriz)) if sumas[i] >= promedio_general]
    return resultado

# === TESTS ===
try:
    assert filtrar_filas_por_promedio([[1, 2], [10, 20], [5, 5, 5]]) == [[10, 20], [5, 5, 5]], "Error: el test 1 ha fallado."
    assert filtrar_filas_por_promedio([[1, 1], [1, 1]]) == [[1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert filtrar_filas_por_promedio([[0, 0], [100, 100]]) == [[100, 100]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")