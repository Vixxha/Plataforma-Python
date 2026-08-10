# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas desordenadas, y devuelva el nombre limpio (sin espacios al inicio y final, todo en minúsculas) y con un prefijo '@' añadido al principio. Si la cadena está vacía o solo contiene espacios, debe devolver una cadena vacía.
# difficulty: Básico
# expected_output: "@python_lover"
# hint: Recuerda usar métodos de strings como strip(), lower() y verificar si el string no está vacío.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    if not nombre_limpio:
        return ""
    return f"@{nombre_limpio.replace(' ', '_')}"

# === TESTS ===
try:
    assert formatear_usuario("  Python Lover  ") == "@python_lover", "Error: el test 1 ha fallado."
    assert formatear_usuario("   ") == "", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("ADMIN") == "@admin", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")