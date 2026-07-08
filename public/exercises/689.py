# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferenciación entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True (para "Anita lava la tina")
# hint: Utiliza un método para filtrar caracteres no alfanuméricos y convierte todo a minúsculas antes de comparar la cadena con su versión invertida.

# === SOLUTION ===
def es_palindromo(texto):
    # Filtramos solo caracteres alfanuméricos y pasamos a minúsculas
    limpio = "".join(char.lower() for char in texto if char.isalnum())
    # Comparamos la cadena con su reverso usando slicing
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")