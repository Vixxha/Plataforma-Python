# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento de votos de cada candidato y, adicionalmente, puedes procesarlo, pero el objetivo principal es contar cuántas veces aparece cada nombre. Sin embargo, para simplificar el test, la función debe retornar el diccionario completo con las frecuencias de cada candidato.
# difficulty: Intermedio
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Utiliza un diccionario para almacenar los conteos. Puedes usar el método .get() del diccionario para manejar candidatos que aún no han sido registrados.

# === SOLUTION ===
def contar_votos(votos):
    recuento = {}
    for candidato in votos:
        recuento[candidato] = recuento.get(candidato, 0) + 1
    return recuento

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")