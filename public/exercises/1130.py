# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que tome una lista de nombres de candidatos a los que se ha votado y devuelva un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {"Ana": 2, "Carlos": 3, "Beatriz": 1}
# hint: Puedes recorrer la lista e ir actualizando el contador de cada candidato en un diccionario, utilizando el método .get() para evitar errores si el candidato aún no ha sido registrado.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Carlos"]) == {"Ana": 2, "Carlos": 3, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")