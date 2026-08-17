# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas de texto representando votos por diferentes candidatos. La función debe retornar un diccionario donde las llaves sean los nombres de los candidatos y los valores sean la cantidad de votos obtenidos. Además, debe retornar el nombre del ganador (en caso de empate, el primero que alcance el máximo de votos según el orden de aparición o cualquier candidato con el máximo). Para este ejercicio, retorna únicamente el diccionario con los conteos.
# difficulty: Intermedio
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes iterar sobre la lista de votos y usar el método .get() del diccionario para inicializar e incrementar el contador de cada candidato.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")