# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una lista de cadenas de texto y devuelva un diccionario donde las claves sean las palabras y los valores sean la cantidad de veces que cada palabra aparece en la lista.
# difficulty: Básico
# expected_output: {'manzana': 2, 'pera': 1}
# hint: Recorre la lista con un bucle y utiliza el método .get() para inicializar o incrementar el contador en el diccionario.

# === SOLUTION ===
def contar_frecuencia(lista_palabras):
    frecuencia = {}
    for palabra in lista_palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia(["manzana", "pera", "manzana"]) == {"manzana": 2, "pera": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia(["a", "a", "a", "b"]) == {"a": 3, "b": 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")