# === METADATA ===
# title: Analizador de Acrónimos Inverso
# description: Crea una función que reciba una cadena de texto y devuelva un acrónimo formado por la primera letra de cada palabra en mayúsculas, seguida de la longitud total de la cadena original entre paréntesis. Ejemplo: "Data Science Python" -> "DSP(19)".
# difficulty: Intermedio
# expected_output: "DSP(19)"
# hint: Utiliza el método .split() para obtener las palabras y considera que los espacios cuentan en la longitud total de la cadena.

# === SOLUTION ===
def generar_acronimo_con_longitud(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    longitud = len(texto)
    return f"{acronimo}({longitud})"

# === TESTS ===
try:
    assert generar_acronimo_con_longitud("Data Science Python") == "DSP(19)", "Error: el test 1 ha fallado."
    assert generar_acronimo_con_longitud("hola mundo") == "HM(10)", "Error: considera casos límites en tu lógica."
    assert generar_acronimo_con_longitud("a b c") == "ABC(5)", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")