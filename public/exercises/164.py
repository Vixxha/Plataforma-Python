# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra, ignorando mayúsculas y signos de puntuación.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto y .split() para dividir la cadena en una lista. Puedes usar el método .replace() para eliminar signos de puntuación comunes.

# === SOLUTION ===
def contar_palabras(texto):
    import re
    # Eliminar puntuación y normalizar a minúsculas
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial, muy genial.") == {'python': 1, 'es': 1, 'genial': 2, 'muy': 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")