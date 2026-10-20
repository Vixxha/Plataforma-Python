# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por guiones bajos ('_') y asegurar que el nombre termine con el sufijo '_dev' (si ya lo tiene, no debe duplicarlo).
# difficulty: Intermedio
# expected_output: "juan_perez_dev"
# hint: Utiliza los métodos de strings de Python como .strip(), .lower(), .replace() y verifica si la cadena termina con un sufijo usando .endswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if not nombre_limpio.endswith("_dev"):
        nombre_limpio += "_dev"
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_dev", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ_DEV") == "maria_gomez_dev", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("py_dev") == "py_dev", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")