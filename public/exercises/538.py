# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Dada una cadena de texto, implementa una función que devuelva un diccionario donde las claves sean las palabras únicas del texto y los valores sean la cantidad de veces que aparecen. Ignora las mayúsculas/minúsculas.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Convierte el texto a minúsculas, utiliza el método split() para separar las palabras y recorre la lista resultante actualizando el diccionario.

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
    assert contar_palabras("Python es genial y Python es divertido") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'divertido': 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("test") == {'test': 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")