# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada una. Ignora las mayúsculas/minúsculas.
# difficulty: Intermedio
# expected_output: {"hola": 2, "mundo": 1}
# hint: Convierte el texto a minúsculas y usa el método split() para separar las palabras antes de iterar.

# === SOLUTION ===
def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial y Python es divertido") == {"python": 2, "es": 2, "genial": 1, "y": 1, "divertido": 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base (cadena vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")