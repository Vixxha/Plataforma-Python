# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y devuelva una nueva lista con los valores restantes escalados multiplicándolos por 1.1 para simular un ajuste de calibración.
# difficulty: Intermedio
# expected_output: [22.0, 27.5, 33.0] para la entrada [20, -5, 25, 30, -10]
# hint: Puedes usar una lista de comprensión (list comprehension) para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [round(t * 1.1, 2) for t in temperaturas if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([20, -5, 25, 30, -10]) == [22.0, 27.5, 33.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-1, -2, -3]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([0, 10]) == [0.0, 11.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")