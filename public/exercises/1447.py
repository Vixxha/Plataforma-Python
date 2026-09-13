# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento de votos de cada candidato y, opcionalmente, podrías contar cuántas veces aparece cada uno. Para este ejercicio, retorna un diccionario donde las llaves sean los nombres y los valores sean el número total de votos que obtuvo cada candidato.
# difficulty: Intermedio
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes recorrer la lista y usar el método get() del diccionario para incrementar el conteo de cada candidato de forma segura.

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")