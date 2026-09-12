# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con posibles espacios y mayúsculas desordenadas. La función debe eliminar los espacios al inicio y al final, convertir todo el texto a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y finalmente agregar el sufijo "@python" al final.
# difficulty: Básico
# expected_output: "juan_perez@python"
# hint: Utiliza los métodos de strings de Python como strip(), lower(), replace() y la concatenación.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_formateado = nombre_limpio.replace(" ", "_")
    return nombre_formateado + "@python"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez@python", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez@python", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("test") == "test@python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")