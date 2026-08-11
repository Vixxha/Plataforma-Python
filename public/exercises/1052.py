# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas representando votos por diferentes candidatos. La función debe retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean la cantidad de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {"Ana": 2, "Juan": 3, "Pedro": 1}
# hint: Puedes usar un bucle para recorrer la lista y el método .get() del diccionario para manejar candidatos que aún no han sido registrados.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        resultado[candidato] = resultado.get(candidato, 0) + 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Juan", "Ana", "Pedro", "Juan", "Juan"]) == {"Ana": 2, "Juan": 3, "Pedro": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Maria", "Maria", "Maria"]) == {"Maria": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")