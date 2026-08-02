# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas de texto representando votos por diferentes candidatos. La función debe retornar un diccionario donde las llaves sean los nombres de los candidatos y los valores sean la cantidad de votos obtenidos por cada uno.
# difficulty: Básico
# expected_output: {"Ana": 3, "Carlos": 2, "Beto": 1}
# hint: Puedes usar un ciclo for para recorrer la lista y el método .get() del diccionario para manejar candidatos que aún no han sido registrados.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        resultado[candidato] = resultado.get(candidato, 0) + 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beto", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beto": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Lucía", "Lucía", "Lucía"]) == {"Lucía": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")