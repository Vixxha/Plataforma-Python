# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente verificar que tenga una longitud mínima de 5 caracteres. Si cumple con la longitud, retorna el string formateado; si no, retorna "Inválido".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Utiliza los métodos de strings de Python como strip(), lower(), replace() y len() para procesar la cadena paso a paso.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if len(nombre_limpio) >= 5:
        return nombre_limpio
    return "Inválido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "Inválido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PYTHON DEVELOPER") == "python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")