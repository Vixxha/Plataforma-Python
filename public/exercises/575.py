# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Dada una cadena de texto, crea una función que devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra (ignorando mayúsculas y minúsculas).
# difficulty: Básico
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .lower() para normalizar el texto y .split() para obtener una lista de palabras.

# === SOLUTION ===
def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial y Python es potente") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'potente': 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")