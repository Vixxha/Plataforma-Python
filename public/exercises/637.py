# === METADATA ===
# title: Transformación de Matriz en Vector
# description: Dada una matriz de números enteros (lista de listas), escribe una función que la convierta en una única lista (vector) que contenga todos los elementos, pero eliminando aquellos valores que sean números pares.
# difficulty: Intermedio
# expected_output: [1, 3, 5, 7]
# hint: Puedes iterar sobre cada fila de la matriz y luego sobre cada elemento, o utilizar una comprensión de listas anidada para filtrar los números impares.

# === SOLUTION ===
def filtrar_impares_matriz(matriz):
    resultado = [num for fila in matriz for num in fila if num % 2 != 0]
    return resultado

# === TESTS ===
try:
    assert filtrar_impares_matriz([[1, 2], [3, 4]]) == [1, 3], "Error: el test 1 ha fallado."
    assert filtrar_impares_matriz([[2, 4, 6], [8, 10]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_impares_matriz([[1, 3, 5], [7, 9, 11]]) == [1, 3, 5, 7, 9, 11], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")