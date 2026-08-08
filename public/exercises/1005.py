# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas representando votos por diferentes candidatos. La función debe retornar un diccionario donde las llaves son los nombres de los candidatos y los valores son la cantidad total de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {"Ana": 3, "Carlos": 2, "Bea": 1}
# hint: Puedes usar el método .get() del diccionario para manejar candidatos que aún no han sido registrados.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        resultado[candidato] = resultado.get(candidato, 0) + 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Bea": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")