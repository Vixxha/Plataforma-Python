# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de usuario de una red social (un string), elimine los espacios en blanco sobrantes al inicio y al final, convierta todo el texto a minúsculas, y reemplace cualquier espacio interno por un guion bajo '_'. Además, si el nombre no empieza con el prefijo '@', debe agregárselo automáticamente al principio.
# difficulty: Básico
# expected_output: "@juan_perez"
# hint: Puedes usar los métodos de string como strip(), lower(), replace(), y verificar si empieza con '@' usando un operador de pertenencia o startswith().

# === SOLUTION ===
def formatear_usuario(username):
    # Limpiar espacios y convertir a minúsculas
    limpio = username.strip().lower()
    # Reemplazar espacios internos por guiones bajos
    formateado = limpio.replace(" ", "_")
    # Asegurar que comience con '@'
    if not formateado.startswith("@"):
        formateado = "@" + formateado
    return formateado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@MARIA GOMEZ") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("carlos") == "@carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")