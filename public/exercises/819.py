# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Utiliza el método .isalnum() para filtrar caracteres y el slicing [::-1] para invertir la cadena resultante.

# === SOLUTION ===
def es_palindromo(texto):
    texto_limpio = "".join(char.lower() for char in texto if char.isalnum())
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: considera casos con signos de puntuación."
    assert es_palindromo("Hola Mundo") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")