# === METADATA ===
# title: Conteo de Votos y Candidato Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario con el recuento total de votos de cada uno, además de identificar al ganador. La función debe retornar un diccionario con dos claves: "recuento" (el diccionario con los votos por candidato) y "ganador" (el nombre del candidato con más votos). En caso de empate, devuelve cualquiera de los ganadores. Si la lista está vacía, devuelve {"recuento": {}, "ganador": None}.
# difficulty: Intermedio
# expected_output: {"recuento": {"Ana": 3, "Luis": 2}, "ganador": "Ana"}
# hint: Puedes usar un diccionario para acumular los conteos recorriendo la lista, y luego usar la función max() especificando una clave para encontrar al ganador.

# === SOLUTION ===
def contar_votos(votos):
    recuento = {}
    for candidato in votos:
        recuento[candidato] = recuento.get(candidato, 0) + 1
    
    if not recuento:
        ganador = None
    else:
        ganador = max(recuento, key=recuento.get)
        
    return {
        "recuento": recuento,
        "ganador": ganador
    }

# === TESTS ===
try:
    assert contar_votos(["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana"]) == {
        "recuento": {"Ana": 3, "Luis": 2, "Carlos": 1},
        "ganador": "Ana"
    }, "Error: el test 1 ha fallado."
    
    assert contar_votos(["Pedro", "Pedro", "Maria", "Maria"]) == {
        "recuento": {"Pedro": 2, "Maria": 2},
        "ganador": "Pedro"
    }, "Error: considera casos límites en tu lógica."
    
    assert contar_votos([]) == {
        "recuento": {},
        "ganador": None
    }, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")