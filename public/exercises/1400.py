# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de usuario de una red social (un string), elimine los espacios en blanco sobrantes al inicio y al final, convierta todo el texto a minúsculas, reemplace cualquier espacio interno por un guion bajo (_) y asegure que comience con el símbolo '@'. Si ya tiene el '@' al inicio, no debe duplicarlo.
# difficulty: Básico
# expected_output: '@juan_perez'
# hint: Puedes usar los métodos de string como strip(), lower(), replace(), y verificar si el string empieza con '@' usando startswith().

# === SOLUTION ===
def formatear_usuario(username):
    username = username.strip().lower()
    username = username.replace(" ", "_")
    if not username.startswith("@"):
        username = "@" + username
    return username

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@MariaGomez") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ANA  ") == "@ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")