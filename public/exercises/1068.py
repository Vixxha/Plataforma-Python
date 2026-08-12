# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula y las demás en minúscula, y finalmente reemplace los espacios internos por guiones bajos (_).
# difficulty: Básico
# expected_output: "ana_maria_gomez"
# hint: Puedes usar los métodos de strings de Python como strip(), title() o capitalize(), y replace().

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip()
    nombre_formateado = nombre_limpio.title()
    return nombre_formateado.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maria gomez  ") == "Ana_Maria_Gomez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN PEREZ") == "Juan_Perez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("  carlos  ") == "Carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")