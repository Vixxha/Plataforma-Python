# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, crea una función que elimine los valores negativos (errores de sensor) y devuelva una nueva lista con los valores restantes escalados multiplicándolos por 1.1 para simular un ajuste de calibración.
# difficulty: Intermedio
# expected_output: [24.2, 33.0, 27.5]
# hint: Puedes usar una lista de comprensión para filtrar los números positivos y aplicar la operación matemática en un solo paso.

# === SOLUTION ===
def ajustar_temperaturas(lista_temps):
    return [round(t * 1.1, 2) for t in lista_temps if t >= 0]

# === TESTS ===
try:
    assert ajustar_temperaturas([22, -5, 30, 25, -1]) == [24.2, 33.0, 27.5], "Error: el test 1 ha fallado."
    assert ajustar_temperaturas([-10, -20]) == [], "Error: considera casos límites en tu lógica."
    assert ajustar_temperaturas([0, 100]) == [0.0, 110.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")