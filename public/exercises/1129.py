# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena que representa un nombre de usuario, elimine los espacios en blanco al inicio y al final, convierta todo el texto a minúsculas y reemplace cualquier espacio interno por un guion bajo (_). Además, si el nombre de usuario resultante tiene menos de 5 caracteres, debe rellenarse a la izquierda con ceros ('0') hasta alcanzar una longitud exactas de 5 caracteres.
# difficulty: Básico
# expected_output: "00-py"
# hint: Recuerda usar métodos de strings como strip(), lower(), replace() y el método zfill() o el formateo con ceros.

# === SOLUTION ===
def formatear_usuario(username):
    limpio = username.strip().lower().replace(" ", "_")
    return limpio.zfill(5)

# === TESTS ===
try:
    assert formatear_usuario("  Py User  ") == "py_us", "Error: el test 1 ha fallado."
    assert formatear_usuario("Admin") == "admin", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("abc") == "00abc", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")