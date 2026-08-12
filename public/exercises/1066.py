# === METADATA ===
# title: Validador de Nombres de Usuario y Capitalización
# description: Escribe una función que reciba el nombre completo de un usuario como una cadena de texto, elimine los espacios en blanco sobrantes al inicio y al final, ponga en formato título (capitalizando la primera letra de cada nombre y apellido) y finalmente reemplace todos los espacios internos por un guion bajo '_'.
# difficulty: Intermedio
# expected_output: "Juan_Pérez_García"
# hint: Recuerda métodos de strings como strip(), title() y replace().

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    # Limpiamos espacios extremos, aplicamos formato título y reemplazamos espacios
    nombre_limpio = nombre_completo.strip().title()
    return nombre_limpio.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  juan pérez garcía  ") == "Juan_Pérez_García", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("MARÍA JOSÉ lópez") == "María_José_López", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("carlos") == "Carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")