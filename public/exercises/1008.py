# === METADATA ===
# title: Validador y Formateador de Cadenas
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario con espacios sobrantes y capitalización irregular. La función debe eliminar los espacios al principio y al final, poner la primera letra de cada palabra en mayúscula y el resto en minúscula, y finalmente reemplazar cualquier espacio interno por un guion bajo (_).
# difficulty: Intermedio
# expected_output: "Ana_Maria_Gomez"
# hint: Recuerda métodos de strings como strip(), title() o capitalize(), y replace().

# === SOLUTION ===
def formatear_nombre_usuario(texto):
    texto_limpio = texto.strip()
    palabras = texto_limpio.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return "_".join(palabras_capitalizadas)

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maria gomez  ") == "Ana_Maria_Gomez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("CARLOS  ALBERTO") == "Carlos_Alberto", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("lucia") == "Lucia", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")