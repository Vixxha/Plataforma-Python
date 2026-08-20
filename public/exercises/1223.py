# === METADATA ===
# title: Validador de Formato de Nombre Completo
# description: Escribe una función que tome un string con un nombre completo, elimine los espacios sobrantes al inicio y al final, ponga en mayúscula la primera letra de cada palabra y devuelva el nombre formateado correctamente. Si el string está vacío, debe devolver un string vacío.
# difficulty: Básico
# expected_output: "Ana María Gómez"
# hint: Puedes usar los métodos de string de Python como strip(), title() o split() y join().

# === SOLUTION ===
def formatear_nombre(nombre):
    if not nombre or not nombre.strip():
        return ""
    return " ".join([palabra.capitalize() for palabra in nombre.strip().split()])

# === TESTS ===
try:
    assert formatear_nombre("  ana maría gómez  ") == "Ana María Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre("JUAN PÉREZ") == "Juan Pérez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre("   ") == "", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")