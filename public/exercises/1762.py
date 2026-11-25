# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas y reemplazar cualquier espacio interno por un guion bajo '_'. Además, si el nombre resultante tiene menos de 5 caracteres, debe rellenarlo con asteriscos ('*') al final hasta alcanzar una longitud mínima de 5 caracteres.
# difficulty: Intermedio
# expected_output: "ana_maria" para la entrada "  Ana Maria  ", y "abc**" para la entrada "abc"
# hint: Recuerda utilizar métodos de strings como strip(), lower(), replace() y considerar cómo rellenar la cadena si su longitud es menor a 5.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_procesado = nombre.strip().lower().replace(" ", "_")
    if len(nombre_procesado) < 5:
        nombre_procesado = nombre_procesado.ljust(5, '*')
    return nombre_procesado

# === TESTS ===
try:
    assert formatear_usuario("  Ana Maria  ") == "ana_maria", "Error: el test 1 ha fallado."
    assert formatear_usuario("DEV") == "dev**", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("Pythonista") == "pythonista", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")