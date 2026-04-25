# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y retorne una nueva lista con los valores restantes multiplicados por 1.1 (ajuste de calibración), redondeados a dos decimales.
# difficulty: Intermedio
# expected_output: [22.55, 33.11, 28.05]
# hint: Puedes usar una lista por comprensión para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(lista_temps):
    return [round(t * 1.1, 2) for t in lista_temps if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([20.5, -5, 30.1, -10, 25.5]) == [22.55, 33.11, 28.05], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-1, -2, -3]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([0, 10]) == [0.0, 11.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")