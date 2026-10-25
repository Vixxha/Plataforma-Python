# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente asegurar que el nombre comience con el prefijo "user_". Si el nombre ya comienza con ese prefijo, no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "user_juan_perez"
# hint: Utiliza métodos de strings como strip(), lower(), replace(), y verifica si la cadena empieza con el prefijo usando startswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    prefijo = "user_"
    if not nombre_limpio.startswith(prefijo):
        return prefijo + nombre_limpio
    return nombre_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "user_juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("user_maria_gomez") == "user_maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("CARLOS RUIZ") == "user_carlos_ruiz", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")