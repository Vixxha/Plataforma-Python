# === METADATA ===
# title: Analizador de Palíndromos Limpios
# description: Escribe una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Utiliza un bucle o una comprensión de listas para filtrar solo caracteres alfanuméricos y conviértelos a minúsculas antes de comparar la cadena con su versión invertida.

# === SOLUTION ===
def es_palindromo(texto):
    # Filtramos solo caracteres alfanuméricos y pasamos a minúsculas
    limpio = "".join(char.lower() for char in texto if char.isalnum())
    # Comparamos con su reverso
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")