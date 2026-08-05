# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas de texto representando votos por diferentes candidatos. La función debe retornar un diccionario donde las llaves sean los nombres de los candidatos y los valores sean la cantidad de votos obtenidos.
# difficulty: Básico
# expected_output: {"Ana": 2, "Carlos": 3, "Bea": 1}
# hint: Puedes recorrer la lista de votos y usar el método `.get()` del diccionario o un bloque `if/else` para actualizar el conteo de cada candidato.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Carlos"]) == {"Ana": 2, "Carlos": 3, "Bea": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")