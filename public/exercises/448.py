# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras como secuencias separadas por espacios).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .split() para separar la cadena y recorrerla con un bucle para actualizar el diccionario.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia_palabras("hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("python es genial y python es potente") == {"python": 2, "es": 2, "genial": 1, "y": 1, "potente": 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")