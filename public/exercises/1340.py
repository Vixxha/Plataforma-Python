# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el conteo de votos de cada candidato y, adicionalmente, puedes implementar la lógica para encontrar al ganador. Para este ejercicio, retorna un diccionario donde las llaves sean los nombres y los valores la cantidad de votos obtenidos.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes recorrer la lista e ir actualizando el conteo en un diccionario utilizando el método .get() para manejar los casos en los que el candidato aún no ha registrado votos.

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