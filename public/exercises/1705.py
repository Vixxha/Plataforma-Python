# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista y retornar un diccionario con el conteo de votos de cada candidato y, además, determinar el ganador. Retorna una tupla con el diccionario de conteo y el nombre del ganador (si hay empate, devuelve cualquiera de los ganadores).
# difficulty: Intermedio
# expected_output: ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana')
# hint: Usa un diccionario para acumular las frecuencias de cada candidato recorriendo la lista, y luego busca la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return conteo, ganador

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana'), "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Maria"]) == ({'Luis': 2, 'Maria': 1}, 'Luis'), "Error: considera casos límites en tu lógica."
    assert contar_votos(["SoloUno"]) == ({'SoloUno': 1}, 'SoloUno'), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")