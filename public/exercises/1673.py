# === METADATA ===
# title: Validador de Nombres de Usuario y Títulos
# description: Escribe una función que tome el nombre completo de un usuario en formato "apellido, nombre", invierta el orden para que quede "Nombre Apellido", elimine espacios sobrantes y capitalice correctamente cada palabra.
# difficulty: Intermedio
# expected_output: "Juan Pérez"
# hint: Puedes usar el método .split() para separar el apellido del nombre usando la coma como delimitador, y el método .title() para las mayúsculas.

# === SOLUTION ===
def formatear_nombre(texto):
    partes = texto.split(",")
    if len(partes) != 2:
        return ""
    apellido = partes[0].strip().title()
    nombre = partes[1].strip().title()
    return f"{nombre} {apellido}"

# === TESTS ===
try:
    assert formatear_nombre("perez, juan") == "Juan Pérez", "Error: el test 1 ha fallado."
    assert formatear_nombre("  GARCÍA LÓPEZ, maría  ") == "María García López", "Error: considera casos límites en tu lógica."
    assert formatear_nombre("rodriguez, alberto") == "Alberto Rodriguez", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")