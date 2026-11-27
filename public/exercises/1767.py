# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula (formato título) y reemplace cualquier espacio interior por un guion bajo (_).
# difficulty: Básico
# expected_output: "ana_maria_gomez"
# hint: Puedes usar los métodos de string de Python como strip(), title(), y split() o replace().

# === SOLUTION ===
def formatear_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip().title()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  ana maria gomez  ") == "Ana_Maria_Gomez", "Error: el test 1 ha fallado."
    assert formatear_usuario("carlos PEREZ") == "Carlos_Perez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("lucía") == "Lucía", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")