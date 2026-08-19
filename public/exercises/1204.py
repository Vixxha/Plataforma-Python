# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas/minúsculas desorganizadas. La función debe eliminar los espacios sobrantes al inicio y al final, convertir todas las letras a minúsculas, y reemplazar cualquier espacio interno por un guion bajo (_).
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Puedes usar los métodos de string de Python como strip(), lower() y replace(), o métodos basados en partición y unión.

# === SOLUTION ===
def formatear_usuario(nombre):
    # Eliminar espacios al inicio y final, pasar a minúsculas y reemplazar espacios internos
    return "_".join(nombre.strip().lower().split())

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA   JOSE") == "maria_jose", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  carlos  ") == "carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")