# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dado una lista de temperaturas (números enteros), crea una función que elimine todas las temperaturas menores a 0, y devuelva una nueva lista con los valores restantes multiplicados por 1.8 para convertirlos a una escala diferente.
# difficulty: Intermedio
# expected_output: [18.0, 36.0, 45.0]
# hint: Puedes usar una lista por comprensión (list comprehension) para filtrar y transformar los elementos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [t * 1.8 for t in temperaturas if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, -5, 20, -1, 25]) == [18.0, 36.0, 45.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20, -30]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([0, 10]) == [0.0, 18.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")