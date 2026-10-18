# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número entero multiplicador. La función debe filtrar los números que sean pares y mayores que cero, y luego multiplicar cada uno de esos números filtrados por el valor del multiplicador. Finalmente, debe retornar la nueva lista con los resultados.
# difficulty: Intermedio
# expected_output: [12, 24]
# hint: Puedes usar una lista por comprensión o un bucle for combinando condiciones lógicas (número > 0 y número % 2 == 0).

# === SOLUTION ===
def filtrar_y_multiplicar(numeros, multiplicador):
    return [num * multiplicador for num in numeros if num > 0 and num % 2 == 0]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, -2, 4, 3, 6], 3) == [12, 18], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([-4, -2, 0, 5], 2) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([2, 4, 6], 5) == [10, 20, 30], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")