# === METADATA ===
# title: Filtrar y Multiplicar Vector
# description: Escribe una función que reciba una lista de números enteros y un número entero multiplicador. La función debe filtrar los números que sean pares, multiplicar cada uno de ellos por el valor del multiplicador, y devolver una nueva lista con los resultados ordenados de menor a mayor.
# difficulty: Intermedio
# expected_output: [4, 12, 16]
# hint: Puedes usar comprensión de listas para filtrar los pares y multiplicar, y luego usar el método sorted() para ordenar el resultado.

# === SOLUTION ===
def filtrar_y_multiplicar(numeros, multiplicador):
    pares_multiplicados = [x * multiplicador for x in numeros if x % 2 == 0]
    return sorted(pares_multiplicados)

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 8], 2) == [4, 8, 16], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([5, 7, 9], 3) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([-2, 5, 0, 3, 4], 5) == [-10, 0, 20], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")