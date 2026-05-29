# === METADATA ===
# title: Analizador de Palíndromos Limpios
# description: Escribe una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "Anita lava la tina", False para "Hola Mundo"
# hint: Utiliza un método para filtrar caracteres alfanuméricos y convierte la cadena a minúsculas antes de comparar con su versión invertida.

# === SOLUTION ===
def es_palindromo(cadena):
    limpia = "".join(caracter.lower() for caracter in cadena if caracter.isalnum())
    return limpia == limpia[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")