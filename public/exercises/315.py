# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza métodos de strings como .lower(), .replace() o .isalnum() para normalizar la cadena antes de compararla con su versión invertida usando slicing [::-1].

# === SOLUTION ===
def es_palindromo(texto):
    # Eliminamos caracteres no alfanuméricos y pasamos a minúsculas
    limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    # Comparamos la cadena limpia con su reverso
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")