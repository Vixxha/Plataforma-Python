# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga en mayúscula la primera letra de cada palabra (formato título), y devuelva un nombre de usuario generado sin espacios y en minúsculas añadiendo un prefijo '@'.
# difficulty: Básico
# expected_output: "@juanperez"
# hint: Puedes usar los métodos de string como .strip(), .title(), .replace() o .lower().

# === SOLUTION ===
def formatear_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip()
    usuario_generado = "@" + nombre_limpio.lower().replace(" ", "")
    return usuario_generado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Pérez  ") == "@juanpérez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARÍA DEL CARMEN") == "@maríadelcarmen", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana gomez ") == "@anagomez", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")