# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con posibles espacios y mezcla de mayúsculas y minúsculas. La función debe eliminar los espacios al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por un guion bajo (_).
# difficulty: Básico
# expected_output: "juan_perez_dev"
# hint: Utiliza los métodos integrados de los strings en Python como strip(), lower() y replace().

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