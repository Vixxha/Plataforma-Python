# === METADATA ===
# title: Contar Vocales
# description: Escribe una función llamada 'contar_vocales' que reciba una cadena de texto y retorne el número total de vocales (a, e, i, o, u) que contiene, ignorando mayúsculas y minúsculas.
# expected_output: Para el texto "Hola Hacker", el resultado esperado es 4.
# hint: Usa el método .lower() en el texto antes de contar para no tener problemas con las mayúsculas y minúsculas.

# === SOLUTION ===
def contar_vocales(texto):
    vocales = "aeiou"
    contador = 0
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    return contador

# === TESTS ===
try:
    assert contar_vocales("Hola Hacker") == 4, "Error: 'Hola Hacker' debe tener 4 vocales"
    assert contar_vocales("Python") == 1, "Error: 'Python' tiene 1 vocal (la 'o')"
    assert contar_vocales("AEIOU") == 5, "Error: Debe contar las vocales en mayúscula correctamente"
    assert contar_vocales("xyz") == 0, "Error: Palabras sin vocales deben devolver 0"
except NameError:
    raise AssertionError("La función 'contar_vocales' no está definida.")
