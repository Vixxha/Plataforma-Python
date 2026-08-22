# === METADATA ===
# title: Conteo y Análisis de Votos
# description: Escribe una función que reciba una lista de strings con los nombres de candidatos votados y devuelva un diccionario con la cantidad de votos que obtuvo cada uno. Además, asegúrate de que el diccionario resultante esté ordenado de mayor a menor según el número de votos (en caso de empate, el orden alfabético de las claves puede ser opcional, pero céntrate en el conteo y ordenamiento descendente por valor). Para mantener el orden, puedes usar un diccionario de Python (que mantiene el orden de inserción desde Python 3.7+).
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes usar un diccionario para contar las frecuencias iterando sobre la lista, y luego ordenar los elementos del diccionario usando sorted() con una función lambda basada en los valores.

# === SOLUTION ===
def contar_y_ordenar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    # Ordenar el diccionario por valor de forma descendente y por clave de forma ascendente en empates
    conteo_ordenado = dict(sorted(conteo.items(), key=lambda item: (-item[1], item[0])))
    return conteo_ordenado

# === TESTS ===
try:
    assert contar_y_ordenar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_y_ordenar_votos(["Zoe", "Ana", "Zoe", "Ana", "Luis"]) == {"Ana": 2, "Zoe": 2, "Luis": 1}, "Error: considera casos límites en tu lógica."
    assert contar_y_ordenar_votos(["Pedro"]) == {"Pedro": 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")