# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, filtra aquellas que sean mayores a 0 grados y devuelve una nueva lista donde cada valor restante sea convertido a grados Fahrenheit (F = C * 9/5 + 32).
# difficulty: Intermedio
# expected_output: [50.0, 68.0, 86.0]
# hint: Puedes utilizar una lista por comprensión (list comprehension) para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    # Filtra valores > 0 y aplica la fórmula de conversión
    return [(t * 9/5 + 32) for t in temperaturas if t > 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, 20, 30]) == [50.0, 68.0, 86.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-5, 0, 5, 10]) == [41.0, 50.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-10, -20]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")