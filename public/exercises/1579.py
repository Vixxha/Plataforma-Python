# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y asegurar que el resultado final termine con el sufijo "_user". Si la cadena original ya termina con "_user" (tras el formateo), no se debe duplicar.
# difficulty: Intermedio
# expected_output: "juan_perez_user"
# hint: Utiliza métodos de strings como strip(), lower(), replace(), y verifica el final con endswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if not nombre_limpio.endswith("_user"):
        nombre_limpio += "_user"
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_user", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA_GOMEZ_user") == "maria_gomez_user", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Ana   Lucia ") == "ana___lucia_user", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")