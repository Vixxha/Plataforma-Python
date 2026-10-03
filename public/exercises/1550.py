# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas y reemplazar cualquier espacio interno por un guion bajo '_'. Además, debe verificar que el resultado final tenga una longitud de al menos 5 caracteres y devuelva el string formateado, o una cadena vacía si no cumple con el requisito de longitud mínima.
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Recuerda usar métodos de strings como strip(), lower(), replace() y len().

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower().replace(" ", "_")
    if len(limpio) >= 5:
        return limpio
    return ""

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("Python Developer") == "python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")