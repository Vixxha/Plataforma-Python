# === METADATA ===
# title: Analizador de Acrónimos
# description: Escribe una función que tome una cadena de texto (frase) y devuelva un acrónimo formado por la primera letra de cada palabra, en mayúsculas. Ignora palabras que tengan menos de 3 letras.
# difficulty: Intermedio
# expected_output: "FPI" para "Formación Profesional Intensiva"
# hint: Usa el método .split() para obtener las palabras y verifica la longitud de cada una antes de extraer su primera letra.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = ""
    for palabra in palabras:
        if len(palabra) >= 3:
            acronimo += palabra[0].upper()
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Formación Profesional Intensiva") == "FPI", "Error: el test 1 ha fallado."
    assert generar_acronimo("hola mundo python") == "HP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("un dia de sol") == "DIA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")