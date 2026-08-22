# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena representando un nombre de usuario con posibles espacios y mayúsculas desordenadas, elimine los espacios al inicio y al final, reemplace los espacios internos por guiones bajos, convierta todo el texto a minúsculas y asegure que termine con el sufijo '_v1'.
# difficulty: Básico
# expected_output: "ana_gomez_v1"
# hint: Utiliza los métodos de string de Python como strip(), lower(), replace() y la concatenación.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower().replace(" ", "_")
    return nombre_limpio + "_v1"

# === TESTS ===
try:
    assert formatear_usuario("  Ana Gomez  ") == "ana_gomez_v1", "Error: el test 1 ha fallado."
    assert formatear_usuario("JUAN PEREZ") == "juan_perez_v1", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("maria") == "maria_v1", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")