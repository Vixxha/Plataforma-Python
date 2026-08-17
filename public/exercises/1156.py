# === METADATA ===
# title: Validador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario y verifique si cumple con tres reglas: longitud entre 5 y 12 caracteres (inclusive), solo contiene letras y números (sin espacios ni símbolos especiales), y comienza con una letra. Devuelve True si es válido y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Usuario123", False para "usr_1"
# hint: Puedes usar los métodos de string como .isalnum(), .isalpha(), y la función len(). Recuerda validar el primer carácter específicamente.

# === SOLUTION ===
def validar_usuario(username: str) -> bool:
    if not (5 <= len(username) <= 12):
        return False
    if not username[0].isalpha():
        return False
    if not username.isalnum():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("Usuario123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("usr_1") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("12345") == False, "Error: el caso base falló."
    assert validar_usuario("abc") == False, "Error: el caso base falló."
    assert validar_usuario("Python2023") == True, "Error: el test 5 ha fallado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")