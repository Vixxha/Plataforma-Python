# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número escalar. La función debe retornar una nueva lista donde solo se conserven los números impares de la lista original, pero multiplicados por el valor del escalar.
# difficulty: Intermedio
# expected_output: [3, 15, 7]
# hint: Puedes usar comprensión de listas junto con el operador módulo (%) para identificar los números impares y aplicar la multiplicación.

# === SOLUTION ===
def filtrar_y_multiplicar(vector, escalar):
    return [x * escalar for x in vector if x % 2 != 0]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 5], 3) == [3, 9, 15], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([2, 4, 6, 8], 5) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([-3, 0, 3], 2) == [-6, 6], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")