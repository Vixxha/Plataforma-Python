# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados en una elección. La función debe retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que recibió cada uno. Además, asegúrate de que el diccionario resultante esté ordenado de mayor a menor según la cantidad de votos (puedes usar un diccionario estándar en Python 3.7+ que mantiene el orden de inserción o un diccionario ordenado).
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes usar un diccionario para llevar la cuenta de las frecuencias y la función sorted() junto con el método .items() para ordenar los elementos según los valores antes de reconstruir el diccionario.

# === SOLUTION ===
def contar_y_ordenar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    conteo_ordenado = dict(sorted(conteo.items(), key=lambda item: item[1], reverse=True))
    return conteo_ordenado

# === TESTS ===
try:
    assert contar_y_ordenar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_y_ordenar_votos(["Luis", "Luis", "Luis"]) == {"Luis": 3}, "Error: considera casos límites en tu lógica."
    assert contar_y_ordenar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")