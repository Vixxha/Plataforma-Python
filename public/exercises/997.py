# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena que representa un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por un guion bajo, y devuelva la cadena completamente en minúsculas.
# difficulty: Básico
# expected_output: "juan_perez"
# hint: Recuerda los métodos de strings en Python como strip(), replace(), y lower().

# === SOLUTION ===
def formatear_usuario(username):
    return username.strip().replace(" ", "_").lower()

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GONZALEZ") == "maria_gonzalez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Ana   Maria  ") == "ana___maria", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")