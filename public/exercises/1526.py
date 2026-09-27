# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga en mayúscula la primera letra de cada palabra (formato título), y devuelva un string que combine el primer nombre y la primera letra del apellido separados por un punto (ejemplo: "Juan Pérez" -> "Juan.P"). Si el string solo tiene una palabra, debe devolver esa palabra formateada.
# difficulty: Intermedio
# expected_output: "Maria.G"
# hint: Puedes usar el método .strip(), .title() y .split() para separar el nombre y las palabras fácilmente.

# === SOLUTION ===
def formatear_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip().title()
    partes = nombre_limpio.split()
    
    if len(partes) <= 1:
        return partes[0] if partes else ""
    
    return f"{partes[0]}.{partes[1][0]}"

# === TESTS ===
try:
    assert formatear_usuario("  juan perez  ") == "Juan.P", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "Maria.G", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("carlos") == "Carlos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")