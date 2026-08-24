# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas representando votos por diferentes candidatos. La función debe retornar un diccionario donde las llaves sean los nombres de los candidatos y los valores sean la cantidad de votos que recibió cada uno.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes recorrer la lista e ir actualizando el contador de cada candidato en el diccionario usando el método .get() o verificando si la llave ya existe.

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")