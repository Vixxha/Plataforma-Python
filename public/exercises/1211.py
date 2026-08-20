# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por guiones bajos (_), y asegure que todo el nombre esté en minúsculas.
# difficulty: Intermedio
# expected_output: "juan_perez_dev"
# hint: Recuerda usar métodos de strings de Python como strip(), lower() y replace().

# === SOLUTION ===
def formatear_nombre_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  Juan Perez Dev  ") == "juan_perez_dev", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("PYTHON  master") == "python__master", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("Ana") == "ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")