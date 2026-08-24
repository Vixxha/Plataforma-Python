# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento total de votos de cada candidato y, además, el nombre del candidato ganador (el que tenga más votos). En caso de empate en el primer puesto, devuelve cualquiera de los ganadores. El formato de retorno debe ser una tupla: `(diccionario_conteo, nombre_ganador)`.
# difficulty: Intermedio
# expected_output: ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana')
# hint: Puedes usar un diccionario para llevar la cuenta de las frecuencias recorriendo la lista, y luego buscar la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    ganador = max(conteo, key=conteo.get)
    return conteo, ganador

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana'), "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Maria"]) == ({'Luis': 2, 'Maria': 1}, 'Luis'), "Error: considera casos límites en tu lógica."
    assert contar_votos(["Solo"]) == ({'Solo': 1}, 'Solo'), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")