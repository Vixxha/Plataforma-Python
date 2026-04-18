# === METADATA ===
# title: Invertir una Cadena
# description: Crea una función llamada 'invertir_cadena' que tome una cadena de texto como argumento y la devuelva invertida sin utilizar la función incorporada reversed().
# expected_output: Para el texto 'Hola Mundo', el resultado esperado es 'odnuM aloH'.
# hint: Recuerda que puedes iterar por cada letra de la cadena e ir concatenándolas en orden inverso dentro de una nueva variable.
# === SOLUTION ===
def invertir_cadena(texto):
    resultado = ""
    for caracter in texto:
        resultado = caracter + resultado
    return resultado

# === TESTS ===
try:
    assert invertir_cadena("Hola Mundo") == "odnuM aloH", "Error: 'Hola Mundo' no se invirtió correctamente."
    assert invertir_cadena("Python") == "nohtyP", "Error: 'Python' esperado 'nohtyP'."
    assert invertir_cadena("") == "", "Error: Una cadena vacía debe devolver una cadena vacía."
except NameError:
    raise AssertionError("La función 'invertir_cadena' no está definida. Asegúrate de nombrarla correctamente.")
