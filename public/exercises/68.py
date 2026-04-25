# === METADATA ===
# title: Analizador de Palíndromos Limpios
# description: Escribe una función que determine si una cadena de texto es un palíndromo (se lee igual al derecho y al revés), ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Utiliza métodos de cadena para limpiar el texto y convertirlo a minúsculas antes de compararlo con su versión invertida mediante slicing [::-1].

# === SOLUTION ===
def es_palindromo(texto):
    # Limpiar: convertir a minúsculas y filtrar solo caracteres alfanuméricos
    limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    # Comparar con su reverso
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")