# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba un string con un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por un guion bajo '_', convierta todo el texto a minúsculas y finalmente le agregue el sufijo '@system' al final.
# difficulty: Básico
# expected_output: "juan_perez@system"
# hint: Recuerda los métodos de string en Python como strip(), replace(), lower() y la concatenación.

# === SOLUTION ===
def formatear_usuario(username):
    # Limpiar espacios, reemplazar espacios internos, convertir a minúsculas y concatenar
    limpio = username.strip()
    reemplazado = limpio.replace(" ", "_")
    minusculas = reemplazado.lower()
    return minusculas + "@system"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez@system", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez@system", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  developer  ") == "developer@system", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")