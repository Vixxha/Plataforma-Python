# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra en el texto (ignorando mayúsculas y signos de puntuación básicos).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .split() para separar las palabras y considera convertir todo a minúsculas con .lower() para estandarizar.

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
    assert contar_frecuencia("Python es genial, Python es divertido") == {'python': 2, 'es': 2, 'genial': 1, 'divertido': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base (string vacío) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")