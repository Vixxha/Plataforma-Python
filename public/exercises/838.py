# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas representando votos por diferentes candidatos y devuelva un diccionario donde las claves son los nombres de los candidatos y los valores son el número total de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes recorrer la lista de votos y usar el método `get()` del diccionario o el objeto `collections.Counter` para acumular las frecuencias de manera eficiente.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Luis"]) == {"Luis": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")