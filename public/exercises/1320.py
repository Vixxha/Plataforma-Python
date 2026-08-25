# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y caracteres mezclados, elimine los espacios al inicio y al final, reemplace los espacios internos por guiones bajos (_), convierta todo el texto a minúsculas y finalmente añada un prefijo '@' al inicio.
# difficulty: Intermedio
# expected_output: "@juan_perez"
# hint: Recuerda usar los métodos de string en Python como strip(), replace(), lower() y la concatenación.

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = texto.strip().lower()
    texto_formateado = texto_limpio.replace(" ", "_")
    return "@" + texto_formateado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Python Developer  ") == "@python_developer", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")