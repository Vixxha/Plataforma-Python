# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas desordenadas. La función debe eliminar los espacios al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_") y añadir al final el sufijo "_user".
# difficulty: Intermedio
# expected_output: "juan_perez_user"
# hint: Recuerda utilizar los métodos de strings como strip(), lower(), y replace().

# === SOLUTION ===
def formatear_nombre_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_con_guiones = nombre_limpio.replace(" ", "_")
    return nombre_con_guiones + "_user"

# === TESTS ===
try:
    assert formatear_nombre_usuario("  Juan Perez  ") == "juan_perez_user", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("MARIA GOMEZ") == "maria_gomez_user", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("  ana  ") == "ana_user", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")