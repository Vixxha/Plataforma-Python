# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario con la cantidad de votos obtenidos por cada uno. Además, asegúrate de que devuelva el nombre del candidato con más votos. Si hay un empate o la lista está vacía, debe manejarlo apropiadamente (devuelve una tupla con el diccionario de conteo y el ganador, o "Empate" si aplica). Para simplificar, esta versión solo retornará el diccionario con el conteo y tú debes implementar la lógica básica de diccionarios.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Bea': 1}
# hint: Utiliza un diccionario para almacenar las frecuencias. Puedes usar el método .get(clave, 0) para inicializar los valores que aún no existen en el diccionario.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Bea": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")