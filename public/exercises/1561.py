# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena con el nombre de usuario de una red social. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, y asegurar que empiece con el símbolo '@'. Si el nombre ya tiene el '@' al inicio (después de limpiar espacios), no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "@programador_py"
# hint: Puedes usar los métodos de string como strip(), lower(), startswith() y la concatenación o slicing.

# === SOLUTION ===
def formatear_usuario(username):
    username_limpio = username.strip().lower()
    if not username_limpio.startswith('@'):
        return '@' + username_limpio
    return username_limpio

# === TESTS ===
try:
    assert formatear_usuario("  JuanPerez  ") == "@juanperez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@PYTHON_DEV") == "@python_dev", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  @MariaGomez ") == "@mariagomez", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")