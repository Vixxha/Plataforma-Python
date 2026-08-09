# === METADATA ===
# title: Conteo de Votos y Candidato Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar esta lista utilizando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos (el ganador). En caso de empate, devuelve cualquiera de ellos.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes usar un diccionario para almacenar el conteo de cada candidato iterando sobre la lista, y luego utilizar la función `max()` con una función de clave personalizada (`key`) para encontrar la llave con el valor máximo.

# === SOLUTION ===
def obtener_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Pedro", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Luis", "Luis", "Maria", "Maria", "Maria"]) == "Maria", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sol"]) == "Sol", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")