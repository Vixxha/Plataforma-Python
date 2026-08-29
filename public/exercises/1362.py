# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de un usuario como un string, elimine los espacios en blanco sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula y el resto en minúscula (formato título), y reemplace cualquier espacio interno por un guion bajo '_'.
# difficulty: Básico
# expected_output: "Ana_Maria_Gomez"
# hint: Puedes usar los métodos de string de Python como strip(), title() y replace() para transformar la cadena paso a paso.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip()
    nombre_titulo = nombre_limpio.title()
    return nombre_titulo.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  ana maria gomez  ") == "Ana_Maria_Gomez", "Error: el test 1 ha fallado."
    assert formatear_usuario("JUAN PEREZ") == "Juan_Perez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  carlos  ") == "Carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")