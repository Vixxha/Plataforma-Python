# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas en grados Celsius, desarrolla una función que filtre aquellas menores a 0 (consideradas gélidas) y devuelva una nueva lista con los valores restantes convertidos a grados Fahrenheit (F = C * 9/5 + 32).
# difficulty: Intermedio
# expected_output: [32.0, 41.0, 50.0] para la entrada [0, 5, 10, -5]
# hint: Puedes usar una lista por comprensión o un bucle for, asegurándote de aplicar la fórmula solo a los elementos que cumplen la condición.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [round(t * 9/5 + 32, 2) for t in temperaturas if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([0, 5, 10, -5]) == [32.0, 41.0, 50.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20]) == [], "Error: debería devolver una lista vacía si todos son menores a 0."
    assert procesar_temperaturas([100]) == [212.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")