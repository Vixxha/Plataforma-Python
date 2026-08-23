# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar esta lista usando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos. En caso de empate, puedes devolver cualquiera de ellos.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Usa un diccionario para almacenar las frecuencias de cada candidato iterando sobre la lista, y luego busca la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Luis", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Juan", "Juan", "Pedro"]) == "Pedro", "Error: considera casos límites en tu lógica."
    assert contar_votos(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")