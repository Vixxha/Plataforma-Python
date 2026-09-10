# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por guiones bajos (_), y finalmente verificar que la longitud del resultado esté entre 4 y 15 caracteres (inclusive). Si cumple con la longitud, devuelve el string formateado; si no, devuelve el string "INVALIDO".
# difficulty: Básico
# expected_output: "juan_perez"
# hint: Utiliza métodos de strings como strip(), lower(), replace() y len() para verificar el tamaño.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if 4 <= len(nombre_limpio) <= 15:
        return nombre_limpio
    return "INVALIDO"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "INVALIDO", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("Programador Expert") == "INVALIDO", "Error: el caso base falló."
    assert formatear_usuario("  PY  dev ") == "py__dev", "Error: verifica el reemplazo de espacios múltiples."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")