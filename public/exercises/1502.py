# === METADATA ===
# title: Conteo de Frecuencia de Caracteres
# description: Escribe una función que tome una cadena de texto y devuelva un diccionario donde las claves sean los caracteres únicos de la cadena y los valores sean la cantidad de veces que aparece cada carácter. Los espacios en blanco también deben ser contados.
# difficulty: Intermedio
# expected_output: {'h': 1, 'o': 2, 'l': 1, 'a': 1}
# hint: Puedes iterar sobre cada carácter de la cadena y usar el método .get() del diccionario para incrementar el contador de forma segura.

# === SOLUTION ===
def contar_caracteres(texto):
    frecuencias = {}
    for char in texto:
        frecuencias[char] = frecuencias.get(char, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_caracteres("hola") == {'h': 1, 'o': 1, 'l': 1, 'a': 1}, "Error: el test 1 ha fallado."
    assert contar_caracteres("banana") == {'b': 1, 'a': 3, 'n': 2}, "Error: considera casos límites en tu lógica."
    assert contar_caracteres("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")