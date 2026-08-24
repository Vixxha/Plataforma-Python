# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas desordenadas. La función debe eliminar los espacios al inicio y al final, convertir todo el texto a minúsculas, y reemplazar cualquier espacio interno por un guion bajo '_'.
# difficulty: Básico
# expected_output: 'juan_perez_dev'
# hint: Recuerda los métodos de strings como .strip(), .lower() y .replace().

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = texto.strip().lower()
    return texto_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez Dev  ") == "juan_perez_dev", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("   PYTHON   PROGRAMMER   ") == "python___programmer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")