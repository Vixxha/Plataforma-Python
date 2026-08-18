# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario en formato de string (puede tener espacios adicionales al inicio o al final, y mayúsculas desordenadas), elimine los espacios sobrantes, ponga en mayúscula la primera letra de cada nombre y apellido (Title Case), y finalmente devuelva el nombre formateado.
# difficulty: Intermedio
# expected_output: "Ana María Gómez Pérez"
# hint: Puedes usar los métodos integrados de los strings en Python para manejar los espacios y las mayúsculas/minúsculas.

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    palabras = nombre_completo.strip().split()
    return " ".join([palabra.capitalize() for palabra in palabras])

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maría gómez pérez  ") == "Ana María Gómez Pérez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN PÉREZ") == "Juan Pérez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("dAnIeL dE lA tOrRe") == "Daniel De La Torre", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")