# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de un usuario como un string, elimine los espacios en blanco innecesarios al inicio y al final, reemplace cualquier espacio interno por guiones bajos (_), convierta todo el string a minúsculas y finalmente asegure que comience con el prefijo "@". Si el string ya tiene el prefijo, no debe duplicarlo.
# difficulty: Básico
# expected_output: "@juan_perez"
# hint: Puedes usar los métodos de string como strip(), replace(), lower(), y verificar si el string empieza con "@" usando startswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if not nombre_limpio.startswith("@"):
        return "@" + nombre_limpio
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@Maria Gomez") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PYTHON DEVELOPER") == "@python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")