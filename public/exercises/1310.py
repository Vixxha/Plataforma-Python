# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar la lista usando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos. Si hay un empate, puedes devolver cualquiera de ellos.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes usar un diccionario para llevar el registro de las frecuencias de cada candidato y luego usar la función max() especificando una clave personalizada.

# === SOLUTION ===
def obtener_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Luis", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Pedro", "Pedro", "Juan", "Juan", "Juan"]) == "Juan", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")