# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas desorganizadas. La función debe eliminar los espacios sobrantes al inicio y al final, reemplazar los espacios internos por guiones bajos (_), convertir todo el texto a minúsculas y asegurar que termine con el sufijo "_activo".
# difficulty: Intermedio
# expected_output: "juan_perez_activo"
# hint: Recuerda usar los métodos de strings como strip(), lower(), split() o replace() para limpiar y transformar la cadena paso a paso.

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = texto.strip().lower()
    texto_reemplazado = "_".join(texto_limpio.split())
    return texto_reemplazado + "_activo"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_activo", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA   GOMEZ") == "maria_gomez_activo", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ana ") == "ana_activo", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")