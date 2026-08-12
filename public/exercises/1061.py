# === METADATA ===
# title: Validador y Formateador de Cadenas
# description: Escribe una función que tome una cadena de texto representando un nombre completo, elimine los espacios en blanco innecesarios al inicio y al final, ponga en mayúscula la primera letra de cada palabra y devuelva el resultado en formato de título. Además, si la cadena está vacía o solo contiene espacios, debe retornar "Nombre no válido".
# difficulty: Básico
# expected_output: "Juan Carlos Pérez"
# hint: Puedes usar los métodos de string de Python como strip(), title() y verificar si la cadena está vacía después de limpiar los espacios.

# === SOLUTION ===
def formatear_nombre(texto):
    if not texto or not texto.strip():
        return "Nombre no válido"
    return texto.strip().title()

# === TESTS ===
try:
    assert formatear_nombre("  juan carlos pérez  ") == "Juan Carlos Pérez", "Error: el test 1 ha fallado."
    assert formatear_nombre("   ") == "Nombre no válido", "Error: considera casos límites en tu lógica."
    assert formatear_nombre("MARÍA GARCÍA") == "María García", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")