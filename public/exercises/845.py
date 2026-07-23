# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de usuario de una red social (un string), elimine los espacios en blanco al inicio y al final, lo convierta completamente a minúsculas y reemplace cualquier espacio interno por guiones bajos (_).
# difficulty: Básico
# expected_output: "juan_perez_dev"
# hint: Recuerda usar los métodos de strings de Python como strip(), lower() y replace().

# === SOLUTION ===
def formatear_usuario(username):
    # Eliminar espacios extremos, pasar a minúsculas y reemplazar espacios internos
    return username.strip().lower().replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez Dev  ") == "juan_perez_dev", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana  ") == "ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")