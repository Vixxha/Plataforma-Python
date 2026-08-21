# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena con un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por un guion bajo (_), convierta todo el texto a minúsculas y finalmente le añada el sufijo '@python' al final.
# difficulty: Básico
# expected_output: 'juan_perez@python'
# hint: Recuerda usar los métodos de strings como strip(), replace(), lower() y la concatenación.

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = texto.strip()
    texto_reemplazado = texto_limpio.replace(" ", "_")
    texto_minusculas = texto_reemplazado.lower()
    return texto_minusculas + "@python"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez@python", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez@python", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Ana   Lucia  ") == "ana___lucia@python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")