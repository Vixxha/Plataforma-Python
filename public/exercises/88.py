# === METADATA ===
# title: Analizador de Palíndromos Limpios
# description: Escribe una función que determine si una cadena es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True para "A man, a plan, a canal: Panama", False para "Hola Mundo"
# hint: Considera utilizar los métodos .isalnum() para filtrar caracteres y .lower() para estandarizar la cadena.

# === SOLUTION ===
def es_palindromo(texto):
    filtrado = "".join(char.lower() for char in texto if char.isalnum())
    return filtrado == filtrado[::-1]

# === TESTS ===
try:
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("race a car") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("12321") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")