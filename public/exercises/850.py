# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas desordenadas, limpie los espacios sobrantes de los extremos, convierta todo el texto a minúsculas y reemplace cualquier espacio interno por un guion bajo (_).
# difficulty: Básico
# expected_output: "juan_perez_gomez"
# hint: Utiliza los métodos de strings de Python para eliminar espacios, cambiar mayúsculas y reemplazar caracteres.

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = texto.strip()
    texto_minuscula = texto_limpio.lower()
    return texto_minuscula.replace(" ", "_")

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez Gomez  ") == "juan_perez_gomez", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA   LUISA") == "maria___luisa", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  pedro ") == "pedro", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")