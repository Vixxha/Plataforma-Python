# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar la lista y retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvo cada uno. Además, asegúrate de que el diccionario resultante esté ordenado por número de votos de mayor a menor (puedes usar un dict de Python 3.7+ que mantiene el orden de inserción tras ordenar los elementos).
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes usar un diccionario para contar las frecuencias recorriendo la lista, y luego ordenar los elementos usando la función sorted() junto con un diccionario nuevo o collections.OrderedDict.

# === SOLUTION ===
def contar_y_ordenar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    # Ordenar el diccionario por el valor (votos) de forma descendente
    conteo_ordenado = dict(sorted(conteo.items(), key=lambda item: item[1], reverse=True))
    return conteo_ordenado

# === TESTS ===
try:
    assert contar_y_ordenar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_y_ordenar_votos(["Zoe", "Ana", "Zoe"]) == {"Zoe": 2, "Ana": 1}, "Error: considera casos límites en tu lógica."
    assert contar_y_ordenar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")