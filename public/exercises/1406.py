# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar esta lista usando un diccionario para contar las apariciones de cada candidato y retornar el nombre del candidato con más votos. Si hay un empate, retorna cualquiera de ellos.
# difficulty: Básico
# expected_output: "Ana"
# hint: Usa un diccionario para almacenar las frecuencias de cada candidato recorriendo la lista, y luego busca la clave con el valor máximo.

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
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Luis", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Pedro", "Pedro", "Juan", "Juan", "Pedro"]) == "Pedro", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")