# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados en una elección y retorne un diccionario con el recuento de votos de cada uno. Además, si hay votos, puedes incluir el ganador, pero para este ejercicio la función debe retornar un diccionario con el total de votos por candidato.
# difficulty: Intermedio
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes usar un diccionario e iterar sobre la lista. El método .get() de los diccionarios es muy útil para manejar claves que aún no existen.

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