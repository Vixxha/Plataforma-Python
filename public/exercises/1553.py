# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, y reemplazar cualquier espacio interno por guiones bajos (_). Además, si el nombre termina con un número, debe asegurar que haya un guion bajo antes de ese número (ej. "juan2" -> "juan_2"), a menos que ya lo tenga.
# difficulty: Intermedio
# expected_output: "maria_h_2"
# hint: Puedes usar los métodos de string como strip(), lower(), replace() y verificar el último carácter con indexación negativa.

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_formateado = nombre_limpio.replace(" ", "_")
    
    if len(nombre_formateado) > 1 and nombre_formateado[-1].isdigit() and nombre_formateado[-2] != '_':
        nombre_formateado = nombre_formateado[:-1] + "_" + nombre_formateado[-1]
        
    return nombre_formateado

# === TESTS ===
try:
    assert formatear_usuario("  Maria H 2  ") == "maria_h_2", "Error: el test 1 ha fallado."
    assert formatear_usuario("JUAN PEREZ") == "juan_perez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("ana") == "ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")