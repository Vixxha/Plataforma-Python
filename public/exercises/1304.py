# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el conteo de votos de cada candidato y, además, el nombre del candidato ganador. Si hay un empate en el primer lugar, se puede retornar cualquiera de ellos. La estructura de retorno debe ser un diccionario con el formato {"conteo": {candidato: votos, ...}, "ganador": nombre_ganador}.
# difficulty: Intermedio
# expected_output: {"conteo": {"Ana": 3, "Carlos": 2, "Bea": 1}, "ganador": "Ana"}
# hint: Usa un diccionario para acumular los conteos recorriendo la lista, y luego busca la clave con el valor máximo en ese diccionario.

# === SOLUTION ===
def conteo_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = None
    max_votos = -1
    for candidato, total in conteo.items():
        if total > max_votos:
            max_votos = total
            ganador = candidato
            
    return {"conteo": conteo, "ganador": ganador}

# === TESTS ===
try:
    assert conteo_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {"conteo": {"Ana": 3, "Carlos": 2, "Bea": 1}, "ganador": "Ana"}, "Error: el test 1 ha fallado."
    assert conteo_votos(["Luis", "Luis", "Maria"]) == {"conteo": {"Luis": 2, "Maria": 1}, "ganador": "Luis"}, "Error: considera casos límites en tu lógica."
    assert conteo_votos(["Solo"]) == {"conteo": {"Solo": 1}, "ganador": "Solo"}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")