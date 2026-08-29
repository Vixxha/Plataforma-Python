# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvo cada uno. Además, si hay un empate o múltiples candidatos, debe procesar correctamente el conteo usando un diccionario.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes utilizar el método .get() de los diccionarios para incrementar el contador de cada candidato de forma segura, evitando errores si el candidato aún no está registrado.

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