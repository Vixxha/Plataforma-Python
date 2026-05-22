# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y retorne una nueva lista con los valores restantes multiplicados por 1.8 para convertir Celsius a una escala personalizada.
# difficulty: Intermedio
# expected_output: [54.0, 36.0, 72.0] para la entrada [-5, 30, 20, -10, 40]
# hint: Puedes usar una lista de comprensión para filtrar y transformar los elementos en un solo paso.

# === SOLUTION ===
def procesar_temperaturas(lista_temps):
    return [temp * 1.8 for temp in lista_temps if temp >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([-5, 30, 20, -10, 40]) == [54.0, 36.0, 72.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([0, 10, 20]) == [0.0, 18.0, 36.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-1, -2, -3]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")