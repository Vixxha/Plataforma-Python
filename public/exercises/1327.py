# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento total de votos para cada candidato y, además, el nombre del candidato ganador. Para estructurar la respuesta, retorna un diccionario con dos claves: "conteo" (el diccionario con los votos) y "ganador" (un string con el nombre del candidato con más votos). Si hay empate, puedes retornar cualquiera de ellos. Si la lista está vacía, retorna {"conteo": {}, "ganador": None}.
# difficulty: Intermedio
# expected_output: {'conteo': {'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'ganador': 'Ana'}
# hint: Usa un diccionario para llevar la frecuencia de cada nombre y luego itera sobre los elementos para encontrar el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    if not votos:
        return {"conteo": {}, "ganador": None}
    
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
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {'conteo': {'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'ganador': 'Ana'}, "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Luis"]) == {'conteo': {'Luis': 3}, 'ganador': 'Luis'}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {"conteo": {}, "ganador": None}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")