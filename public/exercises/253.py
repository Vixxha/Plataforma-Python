# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True si es palíndromo, False en caso contrario.
# hint: Utiliza métodos de cadena como .lower() y .isalnum() para limpiar el texto antes de compararlo con su versión invertida.

# === SOLUTION ===
def es_palindromo_limpio(texto):
    texto_limpio = "".join(char.lower() for char in texto if char.isalnum())
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo_limpio("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo_limpio("Hola, mundo!") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo_limpio("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")