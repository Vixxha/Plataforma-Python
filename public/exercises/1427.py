# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas/minúsculas incorrectas. La función debe eliminar los espacios al inicio y al final, reemplazar cualquier espacio interno por un guion bajo '_', convertir todo el texto a minúsculas y, finalmente, asegurar que el nombre comience con el prefijo 'user_'. Si el nombre ya comienza con 'user_', no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "user_juan_perez"
# hint: Utiliza los métodos de strings de Python como .strip(), .lower(), .replace(), y verifica si la cadena empieza con un prefijo usando .startswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_reemplazado = nombre_limpio.replace(" ", "_")
    
    if not nombre_reemplazado.startswith("user_"):
        return "user_" + nombre_reemplazado
    return nombre_reemplazado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "user_juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "user_maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("user_carlos") == "user_carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")