# === METADATA ===
# title: Analizador de Palíndromos Limpios
# description: Escribe una función que determine si una cadena de texto es un palíndromo (se lee igual al derecho y al revés). La función debe ignorar espacios, signos de puntuación y diferenciar mayúsculas de minúsculas.
# difficulty: Intermedio
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Utiliza métodos de string como .lower(), .replace() o un bucle para filtrar caracteres alfanuméricos antes de comparar.

# === SOLUTION ===
def es_palindromo(texto):
    import string
    # Limpiamos el texto: quitamos espacios y signos de puntuación
    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    # Comparamos el texto con su versión invertida
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")