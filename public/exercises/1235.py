# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas desordenadas. La función debe limpiar los espacios al inicio y final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por guiones bajos (_) y asegurar que termine con el sufijo "_user".
# difficulty: Intermedio
# expected_output: "juan_perez_user"
# hint: Utiliza los métodos de strings como .strip(), .lower(), .replace() y la concatenación.

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = texto.strip().lower()
    texto_sin_espacios = texto_limpio.replace(" ", "_")
    return texto_sin_espacios + "_user"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_user", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez_user", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana  ") == "ana_user", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")