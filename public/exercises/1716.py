# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar esta lista y retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvieron. Además, si hay un empate o candidatos, simplemente cuenta todas las frecuencias.
# difficulty: Básico
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes recorrer la lista e ir actualizando el diccionario. Utiliza el método `.get(clave, 0)` para manejar de forma sencilla las claves que aún no existen en el diccionario.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        resultado[candidato] = resultado.get(candidato, 0) + 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Luis"]) == {"Luis": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")