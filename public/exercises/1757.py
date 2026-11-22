# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista usando un diccionario para contar cuántos votos obtuvo cada candidato y retornar el nombre del candidato con más votos. En caso de empate, puedes retornar cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Utiliza un diccionario para almacenar los pares `candidato: conteo_votos`. Luego, puedes recorrer el diccionario para encontrar la clave con el valor máximo.

# === SOLUTION ===
def obtener_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert obtener_ganador(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert obtener_ganador(["Pedro", "Pedro", "Juan", "Juan", "Pedro"]) == "Pedro", "Error: considera casos límites en tu lógica."
    assert obtener_ganador(["Sofia"]) == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")