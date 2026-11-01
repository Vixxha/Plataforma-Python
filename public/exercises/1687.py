# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros (vector) y un número entero multiplicador. La función debe retornar una nueva lista que contenga únicamente los números pares del vector original, pero cada uno de ellos multiplicado por el valor dado.
# difficulty: Intermedio
# expected_output: [4, 12, 16] para la entrada ([1, 2, 3, 4, 6, 9], 2)
# hint: Puedes usar comprensión de listas para filtrar los elementos pares (numero % 2 == 0) y aplicar la multiplicación al mismo tiempo.

# === SOLUTION ===
def filtrar_y_multiplicar(vector, multiplicador):
    return [x * multiplicador for x in vector if x % 2 == 0]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 6, 9], 2) == [4, 8, 12], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([5, 7, 9, 11], 3) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([2, 4, 6], 5) == [10, 20, 30], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")