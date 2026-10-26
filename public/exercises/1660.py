# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar esta lista y retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvo cada uno. Finalmente, debe identificar y retornar el nombre del candidato con más votos (si hay empate, puedes retornar cualquiera de los que tengan el máximo). Utiliza una tupla o lista como estructura de retorno si es necesario, o simplemente retorna un diccionario con el resumen. Para simplificar este ejercicio de nivel básico-intermedio, haz que la función devuelva únicamente el diccionario con el conteo de frecuencias.
# difficulty: Básico
# expected_output: {"Ana": 3, "Carlos": 2, "Beatriz": 1}
# hint: Puedes recorrer la lista e ir actualizando el diccionario. Si la clave no existe, inicialízala en 0 (o usa el método .get() de los diccionarios).

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")