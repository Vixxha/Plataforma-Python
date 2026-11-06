# === METADATA ===
# title: Conteo y Frecuencia de Votos
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos en una elección. La función debe retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvo cada uno.
# difficulty: Básico
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes recorrer la lista de candidatos y verificar si cada nombre ya existe en el diccionario. Si existe, incrementa su valor en 1; si no, inicialízalo en 1. También puedes explorar el uso de un diccionario con valores por defecto como 'collections.defaultdict'.

# === SOLUTION ===
def contar_votos(votos):
    resultado = {}
    for candidato in votos:
        if candidato in resultado:
            resultado[candidato] += 1
        else:
            resultado[candidato] = 1
    return resultado

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]) == {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "Error: el test 1 ha fallado."
    assert contar_votos(["Juan", "Juan", "Juan"]) == {"Juan": 3}, "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")