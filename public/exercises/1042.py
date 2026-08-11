# === METADATA ===
# title: Conteo de Frecuencia de Votos
# description: Escribe una función que reciba una lista de cadenas que representan votos para diferentes candidatos y devuelva un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que recibió cada uno.
# difficulty: Básico
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes utilizar el método get() de los diccionarios o un bucle para verificar si la clave ya existe antes de incrementar su contador.

# === SOLUTION ===
def contar_votos(lista_votos):
    conteo = {}
    for candidato in lista_votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Pedro", "Pedro", "Pedro"]) == {"Pedro": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")