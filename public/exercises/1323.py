# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe procesar la lista y retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvo cada uno. Además, asegúrate de que el diccionario esté ordenado (o que el valor máximo sea fácil de identificar), pero para este ejercicio solo se requiere retornar el diccionario con las frecuencias.
# difficulty: Básico
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes utilizar un diccionario para almacenar la cuenta de cada candidato. Si la clave no existe, puedes inicializarla en 0 antes de sumarle 1, o usar el método `.get()` de los diccionarios.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Luis"]) == {"Luis": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")