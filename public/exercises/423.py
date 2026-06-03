# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, filtra aquellas que sean mayores a 0 grados y devuelve una nueva lista donde cada valor restante sea transformado a grados Fahrenheit usando la fórmula (C * 9/5) + 32.
# difficulty: Intermedio
# expected_output: [32.0, 50.0, 68.0]
# hint: Puedes usar una lista de comprensión (list comprehension) para filtrar los elementos mayores a 0 y aplicar la conversión matemática simultáneamente.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [(c * 9/5) + 32 for c in temperaturas if c > 0]

# === TESTS ===
try:
    assert procesar_temperaturas([0, 10, 20]) == [50.0, 68.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-5, -10, 0]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([100, -20, 30]) == [212.0, 86.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")