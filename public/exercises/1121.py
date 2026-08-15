# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario en formato de string (con posibles espacios en exceso al inicio, final o entre palabras), elimine los espacios sobrantes, capitalice correctamente cada palabra (primera letra en mayúscula y el resto en minúsculas) y devuelva el nombre formateado junto con la cantidad de caracteres que tiene el resultado. La función debe retornar un string con el formato "Nombre Apellido (X caracteres)".
# difficulty: Intermedio
# expected_output: "Ana Maria Gomez (15 caracteres)"
# hint: Utiliza los métodos integrados de strings en Python como strip(), split(), join(), y title(), además de la función len() para contar los caracteres.

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    nombre_limpio = " ".join(nombre_completo.strip().split())
    nombre_formateado = nombre_limpio.title()
    resultado = f"{nombre_formateado} ({len(nombre_formateado)} caracteres)"
    return resultado

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana  maria   gomez  ") == "Ana Maria Gomez (15 caracteres)", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN PEREZ") == "Juan Perez (10 caracteres)", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("  carlos  ") == "Carlos (6 caracteres)", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")