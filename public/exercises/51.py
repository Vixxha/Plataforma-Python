# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de cada palabra. Ignora las mayúsculas y considera que las palabras están separadas por espacios.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto y .split() para obtener una lista de palabras, luego itera para poblar el diccionario.

# === SOLUTION ===
def contar_frecuencia(texto):
    frecuencia = {}
    palabras = texto.lower().split()
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial y python es divertido") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'divertido': 1}, "Error: considera la normalización de mayúsculas."
    assert contar_frecuencia("") == {}, "Error: el caso base de una cadena vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")