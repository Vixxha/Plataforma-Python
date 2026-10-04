# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar esta lista usando un diccionario para contar cuántos votos obtuvo cada candidato y retornar el nombre del candidato con más votos. Si hay un empate o la lista está vacía, debe retornar un mensaje específico o manejarlo adecuadamente.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Usa un diccionario para almacenar las frecuencias de cada nombre y luego busca la clave con el valor máximo.

# === SOLUTION ===
def contar_y_encontrar_ganador(votos):
    if not votos:
        return None
    
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert contar_y_encontrar_ganador(["Ana", "Carlos", "Ana", "Bea", "Ana", "Carlos"]) == "Ana", "Error: el test 1 ha fallado."
    assert contar_y_encontrar_ganador(["Luis", "Luis", "Maria", "Maria", "Maria"]) == "Maria", "Error: considera casos límites en tu lógica."
    assert contar_y_encontrar_ganador([]) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")