# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar la lista usando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos. En caso de empate, puede devolver cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes utilizar un diccionario para almacenar los conteos (clave: nombre, valor: número de votos) y luego iterar sobre él para encontrar la clave con el valor máximo.

# === SOLUTION ===
def obtener_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = None
    max_votos = -1
    for candidato, total in conteo.items():
        if total > max_votos:
            max_votos = total
            ganador = candidato
            
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Luis", "Luis", "Maria", "Maria", "Luis"]) == "Luis", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["SoloUno"]) == "SoloUno", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")