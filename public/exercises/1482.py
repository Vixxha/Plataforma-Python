# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas de texto representando votos para diferentes candidatos y devuelva un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que obtuvo cada uno.
# difficulty: Básico
# expected_output: {"Ana": 3, "Luis": 2, "Carlos": 1}
# hint: Puedes recorrer la lista e ir actualizando el contador de cada candidato en el diccionario, utilizando el método .get() para manejar los casos en que el candidato aún no esté registrado.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        resultado[candidato] = resultado.get(candidato, 0) + 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana"]) == {"Ana": 3, "Luis": 2, "Carlos": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")