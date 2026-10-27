# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena con el nombre de usuario de una red social. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y asegurar que empiece con el símbolo "@". Si ya empieza con "@", no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "@juan_perez"
# hint: Utiliza los métodos integrados de strings de Python como strip(), lower(), replace(), y verifica el primer carácter con un condicional o rebanado (slicing).

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower()
    limpio = limpio.replace(" ", "_")
    if not limpio.startswith("@"):
        limpio = "@" + limpio
    return limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@MARIA GOMEZ") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("carlos") == "@carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")