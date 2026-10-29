# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas y reemplazar cualquier espacio interno por un guion bajo '_'. Además, si el nombre resultante tiene menos de 5 caracteres, debe rellenarlo con asteriscos ('*') al final hasta alcanzar una longitud mínima de 5 caracteres.
# difficulty: Intermedio
# expected_output: "ana_maria"
# hint: Recuerda usar métodos de strings como strip(), lower(), replace() y la multiplicación de strings para el relleno.

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower().replace(" ", "_")
    if len(limpio) < 5:
        limpio = limpio + "*" * (5 - len(limpio))
    return limpio

# === TESTS ===
try:
    assert formatear_usuario("  Ana Maria  ") == "ana_maria", "Error: el test 1 ha fallado."
    assert formatear_usuario("BOB") == "bob**", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("dev_python") == "dev_python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")