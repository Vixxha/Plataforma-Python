# === METADATA ===
# title: Filtro de Matrices por Promedio
# description: Dada una matriz (lista de listas) de números enteros, devuelve una lista con los elementos que sean estrictamente mayores al promedio de todos los números presentes en la matriz.
# difficulty: Intermedio
# expected_output: [5, 6, 8, 9] (para una matriz donde el promedio es menor a esos valores)
# hint: Primero calcula la suma total y cuenta cuántos elementos hay en total para obtener el promedio. Luego, recorre la matriz nuevamente para filtrar los valores.

# === SOLUTION ===
def filtrar_mayores_al_promedio(matriz):
    elementos = [num for fila in matriz for num in fila]
    if not elementos:
        return []
    
    promedio = sum(elementos) / len(elementos)
    return [num for num in elementos if num > promedio]

# === TESTS ===
try:
    assert filtrar_mayores_al_promedio([[1, 2], [3, 4]]) == [4], "Error: el test 1 ha fallado."
    assert filtrar_mayores_al_promedio([[10, 10], [10, 10]]) == [], "Error: considera casos donde no hay elementos mayores al promedio."
    assert sorted(filtrar_mayores_al_promedio([[1, 5], [9, 3]])) == [5, 9], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")