# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que cada palabra aparece en el texto. Considera el texto en minúsculas y sin signos de puntuación.
# difficulty: Intermedio
# expected_output: {"hola": 2, "mundo": 1}
# hint: Usa el método .split() para obtener las palabras y recuerda limpiar los caracteres especiales usando .replace() o un bucle.

# === SOLUTION ===
def contar_palabras(texto):
    texto = texto.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial. Python es divertido!") == {"python": 2, "es": 2, "genial": 1, "divertido": 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")