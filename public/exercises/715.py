# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dado una lista de temperaturas (números enteros), crea una función que elimine todos los valores negativos y devuelva una nueva lista con los valores restantes multiplicados por 1.8 para convertirlos a una escala relativa.
# difficulty: Intermedio
# expected_output: [18.0, 36.0, 45.0] para la entrada [-5, 10, 20, 25]
# hint: Puedes usar una lista por comprensión (list comprehension) para filtrar y transformar los elementos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [temp * 1.8 for temp in temperaturas if temp >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([-5, 10, 20, 25]) == [18.0, 36.0, 45.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([0, -10, -20]) == [0.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-1, -2, -3]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")