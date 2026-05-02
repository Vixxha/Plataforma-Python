# === METADATA ===
# title: Analizador de Palíndromos Sensible
# description: Crea una función que determine si una cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda), ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza un método para filtrar caracteres no alfanuméricos y convierte todo a minúsculas antes de comparar la cadena con su versión invertida usando slicing [::-1].

# === SOLUTION ===
def es_palindromo(texto):
    import re
    limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")