# === METADATA ===
# title: Analizador y Validador de Nombre de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario y verifique si cumple con las siguientes reglas: debe tener entre 5 y 12 caracteres (inclusives), no contener espacios y estar completamente en minúsculas. Si cumple con todo, retorna True; de lo contrario, retorna False.
# difficulty: Intermedio
# expected_output: True o False según corresponda.
# hint: Utiliza métodos de strings como .islower(), .isspace() o la función len(), además de operadores lógicos.

# === SOLUTION ===
def validar_usuario(usuario):
    if not (5 <= len(usuario) <= 12):
        return False
    if not usuario.islower():
        return False
    if " " in usuario:
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("python123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("User123") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("abc") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")