# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario con la cantidad de votos obtenidos por cada uno. Además, asegúrate de que el diccionario resultante esté ordenado de mayor a menor según los votos obtenidos (en Python 3.7+, los diccionarios preservan el orden de inserción). Si hay un empate en el primer puesto, devuelve alfabéticamente el primero.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes usar un diccionario para contar las frecuencias iterando sobre la lista, y luego usar la función sorted() junto con un diccionario para reconstruirlo ordenado por los valores de forma descendente.

# === SOLUTION ===
def contar_y_ordenar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    # Ordenar por cantidad de votos (descendente) y luego por nombre (alfabético)
    candidatos_ordenados = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))
    
    return dict(candidatos_ordenados)

# === TESTS ===
try:
    assert contar_y_ordenar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_y_ordenar_votos(["Zoe", "Ana", "Zoe", "Ana"]) == {"Ana": 2, "Zoe": 2}, "Error: considera casos límites en tu lógica."
    assert contar_y_ordenar_votos(["Pedro"]) == {"Pedro": 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")