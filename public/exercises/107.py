# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferenciación entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Utiliza métodos de string como .lower() y .replace() o isalnum() para filtrar los caracteres no deseados antes de comparar la cadena con su versión invertida.

# === SOLUTION ===
def es_palindromo(texto):
    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")