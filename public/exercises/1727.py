# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por un guion bajo (_). Además, si el nombre resultante tiene menos de 4 caracteres, debe retornar una cadena vacía.
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Recuerda utilizar métodos de strings como strip(), lower(), replace(), y verificar la longitud con len().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if len(nombre_limpio) < 4:
        return ""
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("MARIA LOPEZ") == "maria_lopez", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")