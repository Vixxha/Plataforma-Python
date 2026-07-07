# === METADATA ===
# title: Frecuencia de Caracteres
# description: Crea una función que reciba un string y devuelva un diccionario donde las claves sean los caracteres y los valores sean la cantidad de veces que aparecen en el string. Ignora espacios en blanco.
# difficulty: Básico
# expected_output: {'h': 1, 'o': 2, 'l': 1, 'a': 1} para el input 'hola o'
# hint: Itera sobre la cadena y usa el método .get() del diccionario o una sentencia if para incrementar el contador.

# === SOLUTION ===
def contar_caracteres(texto):
    frecuencia = {}
    for caracter in texto:
        if caracter != " ":
            frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_caracteres("hola") == {'h': 1, 'o': 1, 'l': 1, 'a': 1}, "Error: el test 1 ha fallado."
    assert contar_caracteres("banana") == {'b': 1, 'a': 3, 'n': 2}, "Error: considera casos con letras repetidas."
    assert contar_caracteres("a b a") == {'a': 2, 'b': 1}, "Error: el caso con espacios falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")