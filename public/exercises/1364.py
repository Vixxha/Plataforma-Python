# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre de un usuario como un string, elimine los espacios en blanco sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula y el resto en minúscula, y finalmente reemplace cualquier espacio interno por un guion bajo (_).
# difficulty: Básico
# expected_output: "ana_maria_gomez"
# hint: Puedes utilizar métodos de strings como strip(), title() o capitalize(), y replace() para transformar la cadena paso a paso.

# === SOLUTION ===
def formatear_usuario(nombre: str) -> str:
    nombre_limpio = nombre.strip()
    nombre_titulo = nombre_limpio.title()
    return nombre_titulo.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  ana maria gomez  ") == "Ana_Maria_Gomez", "Error: el test 1 ha fallado."
    assert formatear_usuario("CARLOS PEREZ") == "Carlos_Perez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("lucía") == "Lucía", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")