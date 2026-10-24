# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario con la cantidad de votos obtenidos por cada uno, además de identificar al ganador. Si hay un empate, se debe retornar elfabéticamente el primero. La función debe retornar un diccionario con el formato {"conteo": {candidato: votos}, "ganador": nombre}.
# difficulty: Intermedio
# expected_output: {'conteo': {'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'ganador': 'Ana'}
# hint: Usa un diccionario para acumular frecuencias recorriendo la lista, y luego evalúa los valores máximos para determinar la clave ganadora.

# === SOLUTION ===
def procesar_votacion(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    if not conteo:
        return {"conteo": {}, "ganador": None}
        
    max_votos = max(conteo.values())
    candidatos_max = [c for c, v in conteo.items() if v == max_votos]
    ganador = sorted(candidatos_max)[0]
    
    return {"conteo": conteo, "ganador": ganador}

# === TESTS ===
try:
    assert procesar_votacion(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {'conteo': {'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'ganador': 'Ana'}, "Error: el test 1 ha fallado."
    assert procesar_votacion(["Zack", "Ana", "Zack", "Ana"]) == {'conteo': {'Zack': 2, 'Ana': 2}, 'ganador': 'Ana'}, "Error: considera casos límites en tu lógica."
    assert procesar_votacion([]) == {'conteo': {}, 'ganador': None}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")