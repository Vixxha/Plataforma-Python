# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una lista con todos los elementos de la matriz que sean estrictamente mayores al promedio global de todos los números presentes en la matriz.
# difficulty: Intermedio
# expected_output: [5, 6, 7]
# hint: Primero calcula la suma total y cuenta cuántos elementos hay para obtener el promedio. Luego recorre la matriz nuevamente para filtrar los valores.

# === SOLUTION ===
def filtrar_mayores_al_promedio(matriz):
    if not matriz or not matriz[0]:
        return []
    
    elementos = [num for fila in matriz for num in fila]
    promedio = sum(elementos) / len(elementos)
    
    return [num for num in elementos if num > promedio]

# === TESTS ===
try:
    assert filtrar_mayores_al_promedio([[1, 2], [3, 4]]) == [3, 4], "Error: el test 1 ha fallado."
    assert filtrar_mayores_al_promedio([[10, 10], [10, 10]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_mayores_al_promedio([[1, 5], [2, 8]]) == [5, 8], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")