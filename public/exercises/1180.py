# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto (oración) y devuelva un diccionario donde las claves sean las palabras únicas (en minúsculas y sin puntuación básica) y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Básico
# expected_output: {'python': 2, 'es': 1, 'un': 1, 'lenguaje': 1, 'genial': 1}
# hint: Puedes usar el método .lower(), .split() y un bucle o el método .get() del diccionario para contar las ocurrencias.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    texto_limpio = texto.lower().replace(".", "").replace(",", "")
    palabras = texto_limpio.split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es un lenguaje genial Python") == {'python': 2, 'es': 1, 'un': 1, 'lenguaje': 1, 'genial': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola, hola. Mundo!") == {'hola': 2, 'mundo': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("Test") == {'test': 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")