# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula (formato título) y reemplace los espacios internos por un guion bajo '_'.
# difficulty: Intermedio
# expected_output: "Ana_María_Gómez"
# hint: Puedes usar los métodos de string como strip(), title() y split()/join() o replace().

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip()
    nombre_titulo = nombre_limpio.title()
    return "_".join(nombre_titulo.split())

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maría gómez  ") == "Ana_María_Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN CARLOS PÉREZ") == "Juan_Carlos_Pérez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("  maria  ") == "Maria", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")