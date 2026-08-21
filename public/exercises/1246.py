# === METADATA ===
# title: Conteo de Frecuencia de Caracteres
# description: Escribe una función que tome una cadena de texto y devuelva un diccionario donde las claves sean los caracteres de la cadena y los valores sean la cantidad de veces que aparece cada carácter. Los espacios en blanco también deben ser contados.
# difficulty: Básico
# expected_output: {'h': 1, 'o': 1, 'l': 1, 'a': 1} para la entrada "hola"
# hint: Puedes recorrer la cadena iterando sobre ella y utilizar el método .get() del diccionario para manejar de forma sencilla los caracteres que aparecen por primera vez.

# === SOLUTION ===
def contar_caracteres(texto):
    frecuencias = {}
    for char in texto:
        frecuencias[char] = frecuencias.get(char, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_caracteres("hola") == {'h': 1, 'o': 1, 'l': 1, 'a': 1}, "Error: el test 1 ha fallado."
    assert contar_caracteres("ana") == {'a': 2, 'n': 1}, "Error: considera casos límites en tu lógica."
    assert contar_caracteres("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")