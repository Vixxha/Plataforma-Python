# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas/minúsculas incorrectas. La función debe eliminar los espacios sobrantes al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_") y asegurarse de que termine con el sufijo "_valido".
# difficulty: Intermedio
# expected_output: "juan_perez_valido"
# hint: Utiliza los métodos de strings como strip(), lower(), replace() y la concatenación.

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower()
    formateado = limpio.replace(" ", "_")
    return formateado + "_valido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_valido", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez_valido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  CARLOS  ALBERTO  ") == "carlos__alberto_valido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")