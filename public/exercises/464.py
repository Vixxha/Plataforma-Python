# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista plana con todos los elementos que sean mayores a 10, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [12, 15, 20, 25, 30]
# hint: Puedes recorrer la matriz usando un bucle anidado o una comprensión de listas, y luego aplicar el método sort() o la función sorted().

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
    assert filtrar_y_ordenar([[1, 12], [5, 20], [30, 8]]) == [12, 20, 30], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar([[5, 5], [2, 1]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar([[10, 11], [25, 15], [12, 9]]) == [11, 12, 15, 25], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")