# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de un usuario como una cadena de texto, elimine los espacios en blanco sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula (formato título) y reemplace cualquier espacio interno por un guion bajo '_'.
# difficulty: Intermedio
# expected_output: "Ana_Maria_Perez"
# hint: Puedes usar los métodos integrados de strings en Python como strip(), title() y replace().

# === SOLUTION ===
def formatear_nombre_usuario(nombre):
    nombre_limpio = nombre.strip()
    nombre_titulo = nombre_limpio.title()
    return nombre_titulo.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maria perez  ") == "Ana_Maria_Perez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN CARLOS") == "Juan_Carlos", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("sofia") == "Sofia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")