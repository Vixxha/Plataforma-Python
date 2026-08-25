# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de un usuario como un string, elimine los espacios en blanco innecesarios al inicio y al final, reemplace cualquier espacio interno por un guion bajo (_), convierta todo el texto a minúsculas y finalmente asegure que termine con el sufijo "_valido".
# difficulty: Intermedio
# expected_output: "juan_perez_valido"
# hint: Recuerda usar los métodos de strings como strip(), replace(), lower() y la concatenación.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_formateado = nombre_limpio.replace(" ", "_")
    return nombre_formateado + "_valido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_valido", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez_valido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana  ") == "ana_valido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")