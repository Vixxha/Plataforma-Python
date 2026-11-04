# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente verificar si el resultado tiene una longitud de entre 5 y 15 caracteres (inclusive). Si cumple con la longitud, devuelve el usuario formateado; de lo contrario, devuelve la cadena "Inválido".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Utiliza métodos de strings como strip(), lower(), replace() y valida la longitud usando len().

# === SOLUTION ===
def formatear_usuario(texto):
    usuario_limpio = texto.strip().lower().replace(" ", "_")
    if 5 <= len(usuario_limpio) <= 15:
        return usuario_limpio
    return "Inválido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "Inválido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Maria_Jose  ") == "maria_jose", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")