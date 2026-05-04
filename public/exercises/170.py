# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las llaves sean las palabras y los valores sean la cantidad de veces que aparece cada palabra, ignorando mayúsculas y signos de puntuación.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto y .split() para dividir la cadena. Puedes iterar y actualizar el valor en el diccionario o usar collections.Counter.

# === SOLUTION ===
def contar_frecuencia(texto):
    import re
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial, Python es útil") == {'python': 2, 'es': 2, 'genial': 1, 'útil': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")