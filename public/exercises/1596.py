# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe eliminar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por un guion bajo ('_'). Además, si el nombre resultante tiene menos de 4 caracteres, debe rellenarlo al final con asteriscos ('*') hasta alcanzar una longitud mínima de 4.
# difficulty: Intermedio
# expected_output: "juan_perez" o "ana*"
# hint: Utiliza los métodos de strings de Python como strip(), lower(), replace() y rjust() o la multiplicación de strings para el relleno.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    if len(nombre_limpio) < 4:
        nombre_limpio = nombre_limpio.ljust(4, '*')
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "ana*", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  BOB  ") == "bob*", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")