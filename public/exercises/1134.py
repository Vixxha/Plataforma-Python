# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el conteo total de votos para cada candidato y, además, el nombre del candidato ganador. Si hay un empate, devuelve cualquiera de ellos. La estructura del diccionario resultante debe ser {"conteo": {candidato: votos, ...}, "ganador": nombre_ganador}.
# difficulty: Intermedio
# expected_output: {'conteo': {'Ana': 2, 'Carlos': 3, 'Bea': 1}, 'ganador': 'Carlos'}
# hint: Puedes usar un diccionario para llevar el registro de cuántas veces aparece cada candidato, actualizando el conteo en un bucle, y luego iterar sobre los elementos para encontrar el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
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
    assert contar_votos(["Ana", "Carlos", "Ana", "Carlos", "Carlos", "Bea"]) == {'conteo': {'Ana': 2, 'Carlos': 3, 'Bea': 1}, 'ganador': 'Carlos'}, "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Maria"]) == {'conteo': {'Luis': 2, 'Maria': 1}, 'ganador': 'Luis'}, "Error: considera casos límites en tu lógica."
    assert contar_votos(["SoloUno"]) == {'conteo': {'SoloUno': 1}, 'ganador': 'SoloUno'}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")