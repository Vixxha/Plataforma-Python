# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra en el texto (ignorando mayúsculas).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .lower() para normalizar el texto y .split() para dividir la cadena en una lista de palabras.

# === SOLUTION ===
def contar_frecuencia(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial y Python es facil") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'facil': 1}, "Error: considera casos con múltiples palabras repetidas."
    assert contar_frecuencia("") == {}, "Error: el caso base de cadena vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")