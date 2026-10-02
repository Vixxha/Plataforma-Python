# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena con el nombre de usuario de una red social. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, y asegurar que empiece con el símbolo '@'. Si el nombre ya tiene el '@' al inicio, no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "@programador_py"
# hint: Puedes usar los métodos strip(), lower() ystartswith(), además de concatenación condicional.

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower()
    if not limpio.startswith('@'):
        return '@' + limpio
    return limpio

# === TESTS ===
try:
    assert formatear_usuario("  @Programador_PY  ") == "@programador_py", "Error: el test 1 ha fallado."
    assert formatear_usuario("PYTHON_LOVER") == "@python_lover", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("@DevMaster") == "@devmaster", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")