# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados en una elección y devuelva un diccionario con el conteo de votos de cada uno. Además, asegúrate de que el diccionario esté ordenado (o que el proceso permita identificar la lógica) o simplemente devuelve el conteo total por candidato. Supongamos que queremos que la función devuelva directamente el diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Bea': 1}
# hint: Puedes usar un diccionario para llevar el registro y el método .get() para manejar candidatos que aún no han recibido votos.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Bea": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Luis"]) == {"Luis": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")