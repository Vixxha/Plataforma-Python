# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento total de votos de cada candidato y, además, el nombre del candidato ganador. Si hay un empate o la lista está vacía, debe manejarse adecuadamente según los casos de prueba.
# difficulty: Intermedio
# expected_output: {'votos': {'Ana': 2, 'Carlos': 3}, 'ganador': 'Carlos'}
# hint: Puedes usar un diccionario para contar las frecuencias de cada elemento en la lista y luego iterar sobre él para encontrar la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    if not votos:
        return {"votos": {}, "ganador": None}
    
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    ganador = max(conteo, key=conteo.get)
    
    return {"votos": conteo, "ganador": ganador}

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Carlos", "Carlos"]) == {"votos": {"Ana": 2, "Carlos": 3}, "ganador": "Carlos"}, "Error: el test 1 ha fallado."
    assert contar_votos(["Bea", "Bea", "Luis"]) == {"votos": {"Bea": 2, "Luis": 1}, "ganador": "Bea"}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {"votos": {}, "ganador": None}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")