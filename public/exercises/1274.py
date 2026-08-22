# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas desordenadas. La función debe limpiar los espacios al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y asegurar que termine con el sufijo "_user".
# difficulty: Intermedio
# expected_output: "juan_perez_user"
# hint: Utiliza los métodos de strings strip(), lower(), replace() y la concatenación.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    return nombre_limpio + "_user"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_user", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez_user", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("developer") == "developer_user", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")