# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, y reemplazar cualquier espacio interno por un guion bajo (_). Además, si el nombre resultante tiene menos de 4 caracteres, debe rellenarlo con asteriscos (*) a la derecha hasta alcanzar una longitud de 4.
# difficulty: Intermedio
# expected_output: "juan_perez" (para "  Juan Perez  ") o "abc*" (para "abc")
# hint: Utiliza los métodos de strings de Python como strip(), lower(), replace() y rjust() o concatenación condicional.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if len(nombre_limpio) < 4:
        nombre_limpio = nombre_limpio.ljust(4, '*')
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("ABC") == "abc*", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("   ") == "****", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")