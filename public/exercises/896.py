# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente verificar si cumple con una longitud mínima de 5 caracteres. Si es válido (longitud >= 5), devuelve la cadena formateada; si no es válido, devuelve el string "Usuario inválido".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Utiliza métodos de strings como strip(), lower(), replace(), y la función len() para verificar la longitud.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if len(nombre_limpio) >= 5:
        return nombre_limpio
    return "Usuario inválido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "Usuario inválido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PYTHON DEVELOPER") == "python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")