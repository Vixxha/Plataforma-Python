# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas y reemplazar cualquier espacio interno por un guion bajo '_'. Si el nombre está vacío o solo contiene espacios, debe retornar "inválido".
# difficulty: Básico
# expected_output: "juan_perez"
# hint: Utiliza los métodos de strings de Python como strip(), lower() y replace(), además de verificar si la cadena resultante está vacía.

# === SOLUTION ===
def formatear_usuario(nombre):
    if not nombre or not nombre.strip():
        return "inválido"
    
    nombre_limpio = nombre.strip().lower()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("   ") == "inválido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")