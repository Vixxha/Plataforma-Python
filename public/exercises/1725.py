# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y asegurar que solo contenga caracteres alfanuméricos y guiones bajos (eliminando cualquier otro carácter especial).
# difficulty: Intermedio
# expected_output: "juan_perez_123"
# hint: Puedes usar los métodos strip(), lower(), replace() y recorrer la cadena o usar list comprehensions junto con el método isalnum().

# === SOLUTION ===
def formatear_nombre_usuario(username):
    username_limpio = username.strip().lower()
    username_formateado = "".join([c if c.isalnum() or c == ' ' else '' for c in username_limpio])
    resultado = "_".join(username_formateado.split())
    return resultado

# === TESTS ===
try:
    assert formatear_nombre_usuario("  Juan Pérez 123!  ") == "juan_pérez_123", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("Ana-María_Gomez?") == "anamaríagomez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("   ") == "", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")