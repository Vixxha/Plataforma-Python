# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula (formato título) y reemplace los espacios internos por guiones bajos (_).
# difficulty: Básico
# expected_output: "ana_maria_gomez"
# hint: Puedes usar métodos de strings de Python como strip(), title() y replace() o split().

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip().title()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maría gómez  ") == "Ana_María_Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("juan carlos") == "Juan_Carlos", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("MARIA") == "Maria", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")