# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de cadenas representando los votos emitidos para diferentes candidatos en una elección. La función debe retornar un diccionario con el conteo total de votos por cada candidato y, adicionalmente, el nombre del candidato ganador. Si hay un empate o la lista está vacía, maneja el caso retornando un diccionario vacío o un mensaje adecuado según se especifica en los tests.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Utiliza un diccionario para llevar el conteo de frecuencias. Puedes usar el método .get() o collections.defaultdict para simplificar la acumulación de votos.

# === SOLUTION ===
def contar_votos(votos):
    if not votos:
        return {}
    
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