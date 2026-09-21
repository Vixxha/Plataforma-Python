# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista usando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos. Si hay un empate o la lista está vacía, debe manejarlo apropiadamente (puedes retornar el primer candidato que alcance el máximo o None si está vacía).
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Puedes usar un diccionario para almacenar las frecuencias de cada nombre y luego buscar la clave con el valor máximo utilizando la función `max()` con una función de clave personalizada (`key`).

# === SOLUTION ===
def contar_votos(votos):
    if not votos:
        return None
    
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    ganador = max(conteo, key=conteo.get)
    return ganador

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Maria", "Luis", "Maria", "Luis"]) == "Luis", "Error: considera casos límites en tu lógica."
    assert contar_votos([]) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")