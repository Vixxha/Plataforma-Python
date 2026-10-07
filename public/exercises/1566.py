# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba un string con el nombre de usuario de una red social. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por un guion bajo '_'. Si el nombre está vacío o solo contiene espacios, debe devolver 'usuario_anonimo'.
# difficulty: Intermedio
# expected_output: 'juan_perez_99'
# hint: Puedes usar los métodos de string como .strip(), .lower(), .replace(), y verificar si la cadena resultante está vacía.

# === SOLUTION ===
def formatear_usuario(nombre):
    if not nombre or not nombre.strip():
        return "usuario_anonimo"
    
    nombre_limpio = nombre.strip().lower()
    nombre_formateado = "_".join(nombre_limpio.split())
    
    return nombre_formateado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez 99  ") == "juan_perez_99", "Error: el test 1 ha fallado."
    assert formatear_usuario("ANTONIO   GOMEZ") == "antonio_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("     ") == "usuario_anonimo", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")