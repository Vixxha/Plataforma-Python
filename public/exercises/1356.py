# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento de votos de cada candidato y, opcionalmente, podrías contar cuántas veces aparece cada uno usando diccionarios en Python.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Bea': 1}
# hint: Utiliza un diccionario para almacenar los nombres como claves y las frecuencias como valores. Puedes usar el método .get(clave, 0) para manejar claves que aún no existen en el diccionario.

# === SOLUTION ===
def contar_votos(votos):
    recuento = {}
    for candidato in votos:
        recuento[candidato] = recuento.get(candidato, 0) + 1
    return recuento

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Bea": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")