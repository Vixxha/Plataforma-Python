# === METADATA ===
# title: Frecuencia de Caracteres
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean los caracteres y los valores la cantidad de veces que aparecen en dicha cadena. Ignora los espacios.
# difficulty: Intermedio
# expected_output: {'h': 1, 'o': 2, 'l': 1, 'a': 1}
# hint: Recorre la cadena con un bucle y utiliza el método .get() del diccionario para gestionar contadores iniciales.

# === SOLUTION ===
def contar_caracteres(texto):
    frecuencia = {}
    for caracter in texto.replace(" ", ""):
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_caracteres("hola") == {'h': 1, 'o': 1, 'l': 1, 'a': 1}, "Error: el test 1 ha fallado."
    assert contar_caracteres("abracadabra") == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}, "Error: considera casos con letras repetidas."
    assert contar_caracteres("  ") == {}, "Error: el caso de espacios vacíos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")