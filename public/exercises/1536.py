# === METADATA ===
# title: Conteo de Votos en Elección
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que obtuvo cada uno.
# difficulty: Básico
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes recorrer la lista de votos y usar el método get() del diccionario para incrementar el contador de cada candidato de forma segura.

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(['Ana', 'Carlos', 'Ana', 'Beatriz', 'Carlos', 'Ana']) == {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}, "Error: el test 1 ha fallado."
    assert contar_votos(['Juan']) == {'Juan': 1}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")