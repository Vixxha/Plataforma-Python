# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número escalar. La función debe filtrar únicamente los números impares de la lista original y, posteriormente, multiplicar cada uno de esos números impares por el valor del escalar. El resultado final debe ser una nueva lista con los valores transformados.
# difficulty: Intermedio
# expected_output: [6, 15, 27] para la entrada ([1, 2, 3, 4, 5, 9], 3)
# hint: Puedes usar una comprensión de lista para verificar si un número es impar (numero % 2 != 0) y aplicar la multiplicación al mismo tiempo.

# === SOLUTION ===
def filtrar_y_multiplicar(vector, escalar):
    return [x * escalar for x in vector if x % 2 != 0]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 5, 9], 3) == [3, 9, 15, 27], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([2, 4, 6, 8], 5) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([-3, 0, 7, 2], 2) == [-6, 14], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")