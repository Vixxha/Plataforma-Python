# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar la lista usando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos. Si hay un empate, devuelve cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Utiliza un diccionario para almacenar las frecuencias de cada candidato y luego recorre el diccionario para encontrar la clave con el valor máximo.

# === SOLUTION ===
def obtener_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = None
    max_votos = -1
    for candidato, total in conteo.items():
        if total > max_votos:
            max_votos = total
            ganador = candidato
            
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Luis", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Pedro", "Pedro", "Juan", "Juan", "Pedro"]) == "Pedro", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")