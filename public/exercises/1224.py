# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de usuario de una red social (un string), elimine los espacios en blanco sobrantes al inicio y al final, convierta todo el texto a minúsculas, reemplace cualquier espacio interno por un guion bajo ("_"), y asegure que comience con el símbolo "@". Si ya comienza con "@", no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "@juan_perez"
# hint: Utiliza los métodos integrados de los strings en Python como strip(), lower(), replace(), y verifica el primer carácter usando slicing o condicionales.

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower().replace(" ", "_")
    if not limpio.startswith("@"):
        limpio = "@" + limpio
    return limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@Maria_Gomez") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PYTHON DEVELOPER") == "@python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")