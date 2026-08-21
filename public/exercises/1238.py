# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas de texto representando votos por diferentes candidatos. La función debe retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que obtuvo cada uno.
# difficulty: Básico
# expected_output: {'Ana': 2, 'Carlos': 3, 'Beatriz': 1}
# hint: Puedes recorrer la lista con un bucle y verificar si la clave ya existe en el diccionario antes de incrementar su valor, o utilizar el método .get().

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Carlos"]) == {"Ana": 2, "Carlos": 3, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")