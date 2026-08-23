# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y capitalización irregular. La función debe eliminar los espacios al inicio y al final, reemplazar cualquier espacio interno por un guion bajo '_', convertir todo el texto a minúsculas y, finalmente, asegurar que termine con el sufijo '_vip' solo si la longitud del nombre base (sin el sufijo) es mayor o igual a 5 caracteres. De lo contrario, no se le añade sufijo.
# difficulty: Intermedio
# expected_output: 'juan_perez_vip' o 'ana'
# hint: Utiliza los métodos strip(), lower(), split(), join() y verifica la longitud de la cadena resultante.

# === SOLUTION ===
def formatear_usuario(texto):
    texto_limpio = "_".join(texto.strip().lower().split())
    if len(texto_limpio) >= 5:
        return texto_limpio + "_vip"
    return texto_limpio

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_vip", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "ana", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("Maria Gomez") == "maria_gomez_vip", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")