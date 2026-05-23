# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras como secuencias de caracteres separadas por espacios).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .split() para obtener una lista de palabras y recorre la lista para poblar el diccionario verificando si la palabra ya existe como llave.

# === SOLUTION ===
def contar_frecuencia(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("python es genial y python es potente") == {"python": 2, "es": 2, "genial": 1, "y": 1, "potente": 1}, "Error: considera casos con múltiples palabras repetidas."
    assert contar_frecuencia("") == {}, "Error: el caso base de cadena vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")