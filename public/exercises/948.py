# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y posibles mayúsculas/minúsculas mezcladas. La función debe eliminar los espacios al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por un guion bajo (_).
# difficulty: Básico-Intermedio
# expected_output: "juan_perez_gomez"
# hint: Recuerda los métodos de strings como strip(), lower() y replace().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez Gomez  ") == "juan_perez_gomez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA LOPEZ") == "maria_lopez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana   maria  ") == "ana___maria", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")