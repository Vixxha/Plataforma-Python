# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza métodos de string como .lower(), .replace() o .isalnum() para normalizar la cadena antes de compararla con su reverso.

# === SOLUTION ===
def es_palindromo(texto):
    # Normalizamos el texto: eliminamos caracteres no alfanuméricos y pasamos a minúsculas
    limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    # Comparamos el string limpio con su versión invertida
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")