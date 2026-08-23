# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de usuario de una red social (un string), elimine los espacios en blanco sobrantes al inicio y al final, convierta todo el texto a minúsculas, y reemplace cualquier espacio interno por un guion bajo '_'.
# difficulty: Básico
# expected_output: "juan_perez_123"
# hint: Puedes usar los métodos de string como strip(), lower() y replace().

# === SOLUTION ===
def formatear_usuario(username):
    # Eliminar espacios extremos, convertir a minúsculas y reemplazar espacios internos
    return username.strip().lower().replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez 123  ") == "juan_perez_123", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("   dev   python   ") == "dev___python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")