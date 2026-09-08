# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas/minúsculas desordenadas. La función debe limpiar los espacios al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por guiones bajos (_) y asegurarse de que termine con el sufijo "_valido".
# difficulty: Intermedio
# expected_output: "juan_perez_valido"
# hint: Puedes usar métodos de strings como strip(), lower(), replace() y la concatenación.

# === SOLUTION ===
def formatear_usuario(nombre):
    limpio = nombre.strip().lower()
    con_guiones = limpio.replace(" ", "_")
    return con_guiones + "_valido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_valido", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ SILVA") == "maria_gomez_silva_valido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Ana  ") == "ana_valido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")