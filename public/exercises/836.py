# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de cadenas de texto, donde cada cadena representa el nombre de un candidato que ha recibido un voto. La función debe procesar esta lista utilizando un diccionario para contar cuántos votos obtuvo cada candidato y devolver el nombre del candidato con más votos. En caso de empate, puedes devolver cualquiera de los ganadores.
# difficulty: Intermedio
# expected_output: "Ana"
# hint: Usa un diccionario para almacenar los conteos (clave: nombre, valor: cantidad) iterando sobre la lista, y luego busca la clave con el valor máximo.

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
    assert contar_y_encontrar_ganador(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == "Ana", "Error: el test 1 ha fallado."
    assert contar_y_encontrar_ganador(["Luis", "Luis", "Maria", "Maria", "Maria"]) == "Maria", "Error: considera casos límites en tu lógica."
    assert contar_y_encontrar_ganador(["SoloUno"]) == "SoloUno", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")