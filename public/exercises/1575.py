# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número entero multiplicador. La función debe retornar una nueva lista que contenga únicamente los números que sean mayores que cero (filtrados), y cada uno de esos números debe estar multiplicado por el valor dado.
# difficulty: Intermedio
# expected_output: [10, 20, 30]
# hint: Puedes usar comprensión de listas para filtrar los elementos mayores que cero y aplicar la multiplicación en un solo paso.

# === SOLUTION ===
def filtrar_y_multiplicar(vector, multiplicador):
    return [x * multiplicador for x in vector if x > 0]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([-2, 5, 0, 3, -1, 2], 2) == [10, 6, 4], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([-5, -10, 0], 3) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([1, 2, 3], 4) == [4, 8, 12], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")