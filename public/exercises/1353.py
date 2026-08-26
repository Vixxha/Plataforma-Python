# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento de votos de cada candidato y, opcionalmente, podrías usar métodos de diccionarios. Sin embargo, para este ejercicio, la función debe retornar estrictamente un diccionario con la estructura `{candidato: total_votos}` y además debe retornar el nombre del candidato ganador. Si hay un empate o la lista está vacía, maneja el caso retornando un diccionario vacío o un mensaje según se indica en los tests. Simplificando: la función debe retornar únicamente el diccionario con la frecuencia de cada candidato.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes recorrer la lista e ir actualizando el diccionario usando el método .get() para manejar claves que aún no existen.

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