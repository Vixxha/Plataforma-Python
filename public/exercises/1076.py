# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario en formato string, elimine los espacios en blanco sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula y las demás en minúscula, y finalmente reemplace todos los espacios internos por guiones bajos (_).
# difficulty: Básico
# expected_output: "ana_maria_gomez"
# hint: Puedes usar los métodos de string de Python como strip(), title() y replace(), o split() y join().

# === SOLUTION ===
def formatear_nombre_usuario(nombre):
    return "_".join(nombre.strip().title().split())

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maría gómez  ") == "Ana_María_Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN PEREZ") == "Juan_Perez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("  carlos  ") == "Carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")