# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas desordenadas, limpie los espacios sobrantes en los extremos, convierta todo el texto a minúsculas y reemplace cualquier espacio interno por un guion bajo (_).
# difficulty: Básico
# expected_output: "juan_perez"
# hint: Investiga los métodos de strings `.strip()`, `.lower()` y `.replace()`.

# === SOLUTION ===
def formatear_usuario(username):
    texto_limpio = username.strip().lower()
    return texto_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Carlos   Alberto ") == "carlos___alberto", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")