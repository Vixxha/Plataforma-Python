# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar esta lista usando un diccionario para contar las frecuencias de los votos y retornar el nombre del candidato con más votos. Si hay un empate, puedes retornar cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes usar un diccionario para almacenar a cada candidato como clave y su número de votos como valor, o utilizar 'collections.Counter'.

# === SOLUTION ===
def obtener_ganador(votos):
    if not votos:
        return None
    
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Luis", "Ana", "Carlos"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Pedro", "Pedro", "Juan", "Juan", "Juan"]) == "Juan", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")