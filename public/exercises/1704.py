# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente verificar si tiene una longitud de entre 5 y 15 caracteres (inclusive). Si cumple con la longitud, devuelve el string formateado; si no, devuelve "Inválido".
# difficulty: Básico
# expected_output: "juan_perez"
# hint: Utiliza métodos de strings como strip(), lower(), replace() y la función len() para verificar el tamaño.

# === SOLUTION ===
def procesar_usuario(username):
    limpio = username.strip().lower().replace(" ", "_")
    if 5 <= len(limpio) <= 15:
        return limpio
    return "Inválido"

# === TESTS ===
try:
    assert procesar_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert procesar_usuario("Ana") == "Inválido", "Error: considera casos límites en tu lógica."
    assert procesar_usuario("Maria_Jose") == "maria_jose", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")