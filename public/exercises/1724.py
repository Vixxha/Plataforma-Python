# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y asegurar que termine con el sufijo "_user". Si la cadena original está vacía, debe retornar "invitado_user".
# difficulty: Intermedio
# expected_output: "juan_perez_user"
# hint: Utiliza los métodos de strings como strip(), lower(), replace() y verifica si la cadena está vacía antes de transformar.

# === SOLUTION ===
def formatear_usuario(nombre):
    if not nombre or not nombre.strip():
        return "invitado_user"
    
    nombre_limpio = nombre.strip().lower()
    nombre_reemplazado = nombre_limpio.replace(" ", "_")
    
    if not nombre_reemplazado.endswith("_user"):
        return nombre_reemplazado + "_user"
    return nombre_reemplazado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_user", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ_user") == "maria_gomez_user", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("") == "invitado_user", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")