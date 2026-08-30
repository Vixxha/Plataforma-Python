# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista y retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que obtuvo cada uno.
# difficulty: Intermedio
# expected_output: {'Ana': 2, 'Carlos': 3, 'Beatriz': 1}
# hint: Puedes recorrer la lista de candidatos y utilizar el método .get() del diccionario para incrementar el contador de cada candidato de forma segura.

# === SOLUTION ===
def contar_votos(lista_candidatos):
    votos = {}
    for candidato in lista_candidatos:
        votos[candidato] = votos.get(candidato, 0) + 1
    return votos

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Carlos", "Carlos", "Beatriz"]) == {"Ana": 2, "Carlos": 3, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")