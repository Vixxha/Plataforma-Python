# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas y reemplazar cualquier espacio interno por un guion bajo '_'. Además, si el nombre resultante tiene menos de 4 caracteres, debe rellenarlo con asteriscos '*' al final hasta alcanzar una longitud de 4 caracteres.
# difficulty: Básico
# expected_output: "ana_gomez" o "lu*"
# hint: Utiliza métodos de strings como strip(), lower(), replace() y puedes verificar la longitud con len().

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower().replace(" ", "_")
    if len(limpio) < 4:
        limpio = limpio.ljust(4, '*')
    return limpio

# === TESTS ===
try:
    assert formatear_usuario("  Ana Gomez  ") == "ana_gomez", "Error: el test 1 ha fallado."
    assert formatear_usuario("LU") == "lu**", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PYTHON") == "python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")