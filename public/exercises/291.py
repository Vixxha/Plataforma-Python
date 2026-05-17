# === METADATA ===
# title: Analizador de Palabras Palíndromas
# description: Crea una función que reciba una cadena, elimine los espacios, convierta todo a minúsculas y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# difficulty: Básico
# expected_output: True o False
# hint: Puedes invertir un string en Python utilizando el slicing [::-1] después de limpiar la cadena.

# === SOLUTION ===
def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Python") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("a") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")