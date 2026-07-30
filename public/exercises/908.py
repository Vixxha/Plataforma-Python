# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas representando votos por diferentes candidatos. La función debe retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {"Ana": 3, "Luis": 2, "Carlos": 1}
# hint: Puedes usar un bucle para recorrer la lista y el método .get() del diccionario para manejar valores predeterminados cuando un candidato aparece por primera vez.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana"]) == {"Ana": 3, "Luis": 2, "Carlos": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")