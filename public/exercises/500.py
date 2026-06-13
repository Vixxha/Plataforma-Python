# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferenciación entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza métodos de cadena como .lower(), .replace() o bucles para filtrar caracteres no alfanuméricos antes de comparar la cadena original con su versión invertida.

# === SOLUTION ===
def es_palindromo_limpio(texto):
    import re
    limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo_limpio("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo_limpio("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo_limpio("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")