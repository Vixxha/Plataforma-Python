# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por guiones bajos ('_') y asegurar que el resultado final termine con el sufijo '_valido'.
# difficulty: Intermedio
# expected_output: "juan_perez_valido"
# hint: Recuerda usar métodos de strings como strip(), lower(), replace() y la concatenación.

# === SOLUTION ===
def formatear_nombre_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_modificado = nombre_limpio.replace(" ", "_")
    return nombre_modificado + "_valido"

# === TESTS ===
try:
    assert formatear_nombre_usuario("  Juan Perez  ") == "juan_perez_valido", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("MARIA GOMEZ") == "maria_gomez_valido", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("dev") == "dev_valido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")