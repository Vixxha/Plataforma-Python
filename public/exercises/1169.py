# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por guiones bajos (_), convierta todo el texto a minúsculas y finalmente añada el prefijo "@" al inicio.
# difficulty: Básico
# expected_output: "@juan_perez"
# hint: Puedes usar los métodos de string como strip(), replace(), lower() y la concatenación básica.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_formateado = nombre_limpio.replace(" ", "_")
    return "@" + nombre_formateado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  PyThon DeVeLoPeR  ") == "@python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")