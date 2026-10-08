# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista y retornar un diccionario con el recuento de votos de cada candidato y, opcionalmente, el ganador. En este ejercicio, implementa la función para que devuelva un diccionario con la frecuencia de cada nombre y, además, determina cuál es el candidato con más votos. Si hay un empate o la lista está vacía, maneja el caso retornando un diccionario adecuado o el ganador según corresponda. Específicamente, haz que la función devuelva un diccionario con la estructura {"conteo": {candidato: votos}, "ganador": nombre_ganador}.
# difficulty: Intermedio
# expected_output: {"conteo": {"Ana": 3, "Luis": 2}, "ganador": "Ana"}
# hint: Usa un diccionario para acumular las frecuencias iterando sobre la lista. Luego, puedes usar la función max() pasando una función de clave personalizada (key) para encontrar la clave con el valor máximo.

# === SOLUTION ===
def procesar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    if not conteo:
        return {"conteo": {}, "ganador": None}
    
    ganador = max(conteo, key=conteo.get)
    return {"conteo": conteo, "ganador": ganador}

# === TESTS ===
try:
    assert procesar_votos(["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana"]) == {"conteo": {"Ana": 3, "Luis": 2, "Carlos": 1}, "ganador": "Ana"}, "Error: el test 1 ha fallado."
    assert procesar_votos(["Pedro", "Pedro", "Maria"]) == {"conteo": {"Pedro": 2, "Maria": 1}, "ganador": "Pedro"}, "Error: considera casos límites en tu lógica."
    assert procesar_votos([]) == {"conteo": {}, "ganador": None}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")