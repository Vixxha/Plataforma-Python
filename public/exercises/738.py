# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada una. Ignora mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .split() para obtener las palabras y un bucle para iterar, actualizando el valor en el diccionario si la palabra ya existe o inicializándola en 1.

# === SOLUTION ===
def contar_frecuencia(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial y Python es potente") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'potente': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base (cadena vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")