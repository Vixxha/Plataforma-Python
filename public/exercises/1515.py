# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el conteo total de votos por cada candidato y, además, determinar quién es el ganador. Si hay un empate en el primer puesto, retorna el nombre de cualquiera de ellos. La salida debe ser un diccionario que contenga el conteo ('conteo') y el ganador ('ganador').
# difficulty: Intermedio
# expected_output: {'conteo': {'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'ganador': 'Ana'}
# hint: Puedes usar un diccionario para acumular las frecuencias de cada candidato iterando sobre la lista, y luego buscar la clave con el valor máximo.

# === SOLUTION ===
def procesar_votacion(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get) if conteo else None
    
    return {
        'conteo': conteo,
        'ganador': ganador
    }

# === TESTS ===
try:
    assert procesar_votacion(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {'conteo': {'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'ganador': 'Ana'}, "Error: el test 1 ha fallado."
    assert procesar_votacion(["Luis", "Luis", "Maria"]) == {'conteo': {'Luis': 2, 'Maria': 1}, 'ganador': 'Luis'}, "Error: considera casos límites en tu lógica."
    assert procesar_votacion([]) == {'conteo': {}, 'ganador': None}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")