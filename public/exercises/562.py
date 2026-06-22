# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Crea una función que reciba una lista de temperaturas y devuelva una nueva lista filtrando solo aquellas que sean mayores a 0 y, posteriormente, calculando el valor absoluto de cada una de ellas para asegurar registros positivos.
# difficulty: Intermedio
# expected_output: [5, 12, 3, 20]
# hint: Puedes utilizar una lista por comprensión (list comprehension) o un bucle for, aplicando primero la condición de filtrado y luego la operación de valor absoluto.

# === SOLUTION ===
def procesar_temperaturas(lista_temps):
    return [abs(t) for t in lista_temps if t > 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, -5, 20, 0, -1, 3]) == [10, 20, 3], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20, -30]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([5, 12, 3, 20]) == [5, 12, 3, 20], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")