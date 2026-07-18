# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena es un palíndromo, ignorando espacios, puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "A man, a plan, a canal: Panama"
# hint: Utiliza el método .isalnum() para filtrar caracteres y .lower() para normalizar el texto.

# === SOLUTION ===
def es_palindromo_limpio(texto):
    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo_limpio("A man, a plan, a canal: Panama") == True, "Error: el test 1 ha fallado."
    assert es_palindromo_limpio("race a car") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo_limpio("Anita lava la tina") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")