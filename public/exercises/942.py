# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas y reemplazar cualquier espacio interno por un guion bajo '_'. Además, debe validar que el resultado tenga una longitud mínima de 5 caracteres; si es menor, debe retornar la cadena "INVÁLIDO".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Puedes usar los métodos de string como strip(), lower(), replace() y len() para verificar el tamaño.

# === SOLUTION ===
def formatear_usuario(nombre):
    limpio = nombre.strip().lower().replace(" ", "_")
    if len(limpio) < 5:
        return "INVÁLIDO"
    return limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "INVÁLIDO", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("TEST USER 123") == "test_user_123", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")