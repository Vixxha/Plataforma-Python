# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula (formato título) y reemplace los espacios internos por guiones bajos (_).
# difficulty: Intermedio
# expected_output: "maria_del_carmen"
# hint: Puedes usar los métodos integrados de strings en Python como strip(), title() y replace(), o métodos para dividir y unir palabras.

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip()
    nombre_titulo = nombre_limpio.title()
    return nombre_titulo.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_nombre_usuario("  juan pérez gómez  ") == "Juan_Pérez_Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("MARÍA del CARMEN") == "María_Del_Carmen", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("ana") == "Ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")