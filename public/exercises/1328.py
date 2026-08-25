# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas desordenadas, elimine los espacios al inicio y al final, reemplace los espacios internos por guiones bajos (_), convierta todo el texto a minúsculas y finalmente le añada el sufijo '_v1' al final.
# difficulty: Básico
# expected_output: 'juan_perez_v1'
# hint: Utiliza los métodos de strings de Python como strip(), lower(), y replace().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_formateado = nombre_limpio.replace(" ", "_")
    return nombre_formateado + "_v1"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_v1", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez_v1", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  Ana  ") == "ana_v1", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")