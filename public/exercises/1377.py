# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de un usuario como un string, elimine los espacios en blanco sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula y el resto en minúsculas, y reemplace cualquier espacio interno por un guion bajo '_'.
# difficulty: Básico
# expected_output: "Juan_Carlos_Perez"
# hint: Puedes usar los métodos strip(), title() y replace() de los strings en Python.

# === SOLUTION ===
def formatear_nombre_usuario(nombre):
    nombre_limpio = nombre.strip()
    nombre_capitalizado = nombre_limpio.title()
    return nombre_capitalizado.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  juan carlos perez  ") == "Juan_Carlos_Perez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("MARÍA  JOSÉ") == "María_José", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("pedro") == "Pedro", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")