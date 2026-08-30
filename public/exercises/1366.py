# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista usando un diccionario para contar las frecuencias de cada voto y retornar el nombre del candidato con más votos. Si hay un empate, puede retornar cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Utiliza un diccionario para almacenar el conteo de cada candidato (clave: nombre, valor: número de votos) y luego recorre el diccionario para encontrar la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Maria", "Maria", "Luis"]) == "Luis", "Error: considera casos límites en tu lógica."
    assert contar_votos(["Sol"]) == "Sol", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")