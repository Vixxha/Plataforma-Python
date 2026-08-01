# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas representando votos por diferentes candidatos y devuelva un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que obtuvo cada uno.
# difficulty: Básico
# expected_output: {"Ana": 2, "Carlos": 3, "Beatriz": 1}
# hint: Puedes iterar sobre la lista y usar el método .get() del diccionario para inicializar e incrementar los contadores.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        resultado[candidato] = resultado.get(candidato, 0) + 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Carlos", "Carlos", "Beatriz"]) == {"Ana": 2, "Carlos": 3, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")