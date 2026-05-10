# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza métodos de string como .lower(), .isalnum() y el slicing [::-1] para invertir la cadena.

# === SOLUTION ===
def es_palindromo(cadena):
    # Filtramos la cadena para mantener solo caracteres alfanuméricos y pasarlos a minúsculas
    limpia = "".join(caracter.lower() for caracter in cadena if caracter.isalnum())
    # Comparamos la cadena limpia con su versión invertida
    return limpia == limpia[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")