# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena representando un nombre de usuario con espacios y mayúsculas desorganizadas. La función debe eliminar los espacios al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por un guion bajo '_'.
# difficulty: Básico
# expected_output: "juan_perez"
# hint: Investiga los métodos de strings en Python como strip(), lower() y replace().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GONZALEZ") == "maria_gonzalez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana  ") == "ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")