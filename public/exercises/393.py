# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dado una lista de temperaturas (números enteros), crea una función que elimine todas las temperaturas menores a 0 (consideradas inválidas) y devuelva una nueva lista con los valores restantes multiplicados por 1.8 para convertirlos a una escala distinta.
# difficulty: Intermedio
# expected_output: [18.0, 36.0, 45.0]
# hint: Puedes usar una lista por comprensión (list comprehension) para filtrar y transformar los elementos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [temp * 1.8 for temp in temperaturas if temp >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, -5, 20, 25, -10]) == [18.0, 36.0, 45.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-1, -2, -3]) == [], "Error: debería retornar una lista vacía si todos son negativos."
    assert procesar_temperaturas([0, 100]) == [0.0, 180.0], "Error: el caso base de 0 grados falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")