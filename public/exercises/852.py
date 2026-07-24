# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario en formato de string (con posibles espacios sobrantes al inicio, final o entre palabras), elimine los espacios extras, capitalice correctamente cada palabra (primera letra en mayúscula y el resto en minúsculas) y devuelva el string limpio.
# difficulty: Básico
# expected_output: "Ana María Gómez"
# hint: Puedes usar los métodos integrados de los strings en Python como strip(), split() y join(), combinados con capitalize().

# === SOLUTION ===
def formatear_nombre(nombre_completo):
    palabras = nombre_completo.strip().split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return " ".join(palabras_capitalizadas)

# === TESTS ===
try:
    assert formatear_nombre("  ana  maría   gómez  ") == "Ana María Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre("JUAN PÉREZ") == "Juan Pérez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre("lucía") == "Lucía", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")