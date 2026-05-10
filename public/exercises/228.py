# === METADATA ===
# title: Filtro y Promedio de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista simple con todos los números que sean mayores a 10, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [12, 15, 20]
# hint: Puedes usar un bucle anidado o una comprensión de listas para aplanar la matriz y filtrar los elementos antes de aplicar el método sort().

# === SOLUTION ===
def filtrar_y_ordenar(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_ordenar([[1, 15], [5, 20], [12, 3]]) == [12, 15, 20], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar([[1, 2], [3, 4]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar([[11, 11], [11, 11]]) == [11, 11, 11, 11], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")