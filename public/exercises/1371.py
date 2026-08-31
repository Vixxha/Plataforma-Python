# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar esta lista utilizando un diccionario para contar cuántos votos obtuvo cada candidato y retornar el nombre del candidato con más votos. Si hay un empate, puedes retornar cualquiera de ellos.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes usar un diccionario para almacenar las frecuencias de cada candidato y luego iterar sobre él para encontrar el valor máximo.

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
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Pedro", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Luis", "Luis", "Maria", "Maria", "Maria"]) == "Maria", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["SoloUno"]) == "SoloUno", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")