# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que reciba una cadena, elimine todos los espacios y signos de puntuación, convierta el texto a minúsculas y determine si es un palíndromo (se lee igual al derecho y al revés).
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza el método isalnum() para filtrar caracteres y el slicing [::-1] para invertir la cadena resultante.

# === SOLUTION ===
def es_palindromo(texto):
    cadena_limpia = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return cadena_limpia == cadena_limpia[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")