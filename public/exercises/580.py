# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que reciba una cadena, elimine todos los espacios, convierta el texto a minúsculas y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# difficulty: Básico
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Usa el método .replace() para quitar espacios y el slicing [::-1] para invertir la cadena.

# === SOLUTION ===
def es_palindromo(texto):
    cadena_limpia = texto.replace(" ", "").lower()
    return cadena_limpia == cadena_limpia[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("reconocer") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")