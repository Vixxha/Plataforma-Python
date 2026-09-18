# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario con la cantidad de votos de cada uno. Además, si hay un ganador con la mayoría absoluta o simple, puedes retornar el diccionario de conteo. Para este ejercicio, la función debe retornar el diccionario completo con el conteo de frecuencias de cada candidato.
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Bea': 1}
# hint: Utiliza un bucle para recorrer la lista y el método `.get()` del diccionario para inicializar e incrementar los contadores de forma limpia.

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