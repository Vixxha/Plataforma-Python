# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente asegurar que comience con el prefijo "@". Si ya lo tiene, no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "@juan_perez"
# hint: Utiliza los métodos de strings de Python como strip(), lower(), replace() y verifica si la cadena empieza con '@' usando startswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_modificado = nombre_limpio.replace(" ", "_")
    if not nombre_modificado.startswith("@"):
        return "@" + nombre_modificado
    return nombre_modificado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@MARIA_GOMEZ") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Ana   Maria  ") == "@ana___maria", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")