# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas de texto representando votos por diferentes candidatos y devuelva un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {'Ana': 3, 'Carlos': 2, 'Bea': 1}
# hint: Puedes recorrer la lista e ir actualizando el contador de cada candidato en el diccionario usando el método .get() para evitar errores si el candidato aún no ha sido registrado.

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Bea": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")