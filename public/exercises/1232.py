# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba un string con el nombre de usuario de una red social. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ('_') y asegurar que comience con el símbolo '@'. Si el nombre ya comienza con '@', no debe duplicarlo.
# difficulty: Intermedio
# expected_output: "@juan_perez"
# hint: Puedes usar métodos de strings como .strip(), .lower(), .replace(), y verificar prefijos con .startswith().

# === SOLUTION ===
def formatear_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_sin_espacios = nombre_limpio.replace(" ", "_")
    
    if not nombre_sin_espacios.startswith("@"):
        return "@" + nombre_sin_espacios
    return nombre_sin_espacios

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "@juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("@Maria_Gomez") == "@maria_gomez", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("  ANA  ") == "@ana", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")