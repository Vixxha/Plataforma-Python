# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de usuario de una red social (un string), elimine los espacios en blanco al inicio y al final, lo convierta completamente a minúsculas y reemplace cualquier espacio interno por guiones bajos (_). Además, si el nombre comienza con el símbolo '@', este debe ser eliminado.
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Utiliza los métodos de strings de Python como strip(), lower(), replace() y verifica el primer carácter usando indexación o startswith().

# === SOLUTION ===
def formatear_usuario(username: str) -> str:
    username = username.strip()
    if username.startswith('@'):
        username = username[1:]
    username = username.lower()
    username = username.replace(' ', '_')
    return username

# === TESTS ===
try:
    assert formatear_usuario("  @Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("@PYTHON_DEV") == "python_dev", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")