# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos y devuelva una nueva lista con los valores restantes multiplicados por 1.8 para convertirlos a una escala distinta.
# difficulty: Intermedio
# expected_output: [18.0, 36.0, 45.0]
# hint: Puedes usar una lista por comprensión (list comprehension) para filtrar y transformar los datos en una sola línea de código.

# === SOLUTION ===
def procesar_temperaturas(lista_temps):
    return [t * 1.8 for t in lista_temps if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, 20, 25]) == [18.0, 36.0, 45.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-5, 0, 10]) == [0.0, 18.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-10, -20]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")