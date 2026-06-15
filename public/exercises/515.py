# === METADATA ===
# title: Filtrado de Matriz y Promedio
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista simple con todos los elementos que sean mayores que el promedio de toda la matriz.
# difficulty: Intermedio
# expected_output: [5, 6, 8] (si la matriz es [[1, 2], [5, 6, 8]] y el promedio es 4.4)
# hint: Primero calcula la suma total y la cantidad de elementos totales para hallar el promedio, luego recorre la matriz con un bucle anidado o list comprehension.

# === SOLUTION ===
def filtrar_mayores_al_promedio(matriz):
    elementos = [num for fila in matriz for num in fila]
    if not elementos:
        return []
    
    promedio = sum(elementos) / len(elementos)
    return [num for num in elementos if num > promedio]

# === TESTS ===
try:
    assert filtrar_mayores_al_promedio([[1, 2], [3, 4]]) == [3, 4], "Error: el test 1 ha fallado."
    assert filtrar_mayores_al_promedio([[10, 20], [5, 5]]) == [10, 20], "Error: considera casos límites en tu lógica."
    assert filtrar_mayores_al_promedio([[1, 1], [1, 1]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")