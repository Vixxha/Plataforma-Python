# === METADATA ===
# title: Analizador de Palíndromos Limpios
# description: Escribe una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza el método .isalnum() para filtrar caracteres y el slicing [::-1] para invertir la cadena.

# === SOLUTION ===
def es_palindromo(texto):
    cadena_limpia = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return cadena_limpia == cadena_limpia[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola, mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")