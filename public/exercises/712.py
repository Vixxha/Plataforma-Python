# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferenciación entre mayúsculas y minúsculas.
# difficulty: Básico
# expected_output: True o False
# hint: Utiliza métodos de cadena como .lower(), .isalnum() y compara la cadena con su versión invertida usando slicing [::-1].

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