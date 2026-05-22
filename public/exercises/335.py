# === METADATA ===
# title: Analizador de Palabras Palíndromas
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True si es palíndromo, False en caso contrario.
# hint: Utiliza un método para filtrar caracteres no alfanuméricos y asegúrate de normalizar el texto a minúsculas antes de comparar la cadena con su versión invertida.

# === SOLUTION ===
def es_palindromo(texto):
    import re
    limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")