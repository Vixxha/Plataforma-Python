# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas en grados Celsius, crea una función que elimine todas las temperaturas bajo cero (menores a 0) y devuelva una nueva lista con los valores restantes convertidos a grados Fahrenheit usando la fórmula: (Celsius * 9/5) + 32.
# difficulty: Intermedio
# expected_output: [32.0, 68.0, 100.4]
# hint: Puedes usar una lista de comprensión (list comprehension) para filtrar los elementos y aplicar la fórmula matemática en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [(t * 9/5) + 32 for t in temperaturas if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([0, 20, 38]) == [32.0, 68.0, 100.4], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -5, 5]) == [41.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-1, -2, -3]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")