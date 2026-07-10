# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Crea una función que reciba una lista de temperaturas y devuelva una nueva lista filtrando solo aquellas que sean mayores a 0 y, posteriormente, normalizando los valores restantes restando el valor mínimo del grupo filtrado.
# difficulty: Intermedio
# expected_output: [0, 5, 12] (para una entrada de [-5, 0, 10, 15, 22] el resultado es [0, 5, 12])
# hint: Primero usa una lista de comprensión para filtrar los positivos, luego utiliza las funciones min() y una segunda iteración para normalizar.

# === SOLUTION ===
def normalizar_temperaturas(temperaturas):
    filtradas = [t for t in temperaturas if t > 0]
    if not filtradas:
        return []
    min_val = min(filtradas)
    return [t - min_val for t in filtradas]

# === TESTS ===
try:
    assert normalizar_temperaturas([-5, 0, 10, 15, 22]) == [0, 5, 12], "Error: el test 1 ha fallado."
    assert normalizar_temperaturas([10, 20, 30]) == [0, 10, 20], "Error: considera casos límites en tu lógica."
    assert normalizar_temperaturas([-10, -5, 0]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")