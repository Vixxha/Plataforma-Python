# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar esta lista usando un diccionario para contar las frecuencias de cada candidato y retornar el nombre del candidato con más votos. Si hay un empate, retorna cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes usar un diccionario para llevar el registro de cuántas veces aparece cada nombre. Luego, recorre el diccionario para encontrar la clave con el valor máximo.

# === SOLUTION ===
def obtener_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = None
    max_votos = -1
    for candidato, num_votos in conteo.items():
        if num_votos > max_votos:
            max_votos = num_votos
            ganador = candidato
            
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Pedro", "Pedro", "Juan", "Juan", "Pedro"]) == "Pedro", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")