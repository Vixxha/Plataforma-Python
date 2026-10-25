# === METADATA ===
# title: Validador de Palíndromos Avanzado
# description: Escribe una función que determine si una cadena de texto es un palíndromo (se lee igual hacia adelante que hacia atrás), ignorando los espacios, los signos de puntuación y las mayúsculas/minúsculas.
# difficulty: Básico
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Puedes utilizar métodos de strings como .lower(), .replace() o un enfoque filtrando caracteres alfanuméricos con .isalnum().

# === SOLUTION ===
def es_palindromo(texto):
    # Limpiar el texto: convertir a minúsculas y filtrar solo caracteres alfanuméricos
    texto_limpio = "".join(c.lower() for c in texto if c.isalnum())
    # Comparar el texto limpio con su reverso
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: considera casos límites en tu lógica."
    assert es_palindromo("Hola Mundo") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")