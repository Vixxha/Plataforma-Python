# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que tome un string que representa un nombre de usuario y verifique si cumple con las reglas: debe tener entre 5 y 15 caracteres (inclusive), solo contener letras minúsculas y números (sin espacios ni símbolos especiales), y no debe empezar con un número. La función debe retornar True si es válido y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False según corresponda.
# hint: Puedes usar métodos de string como .isalnum(), .islower() y verificar la longitud con len().

# === SOLUTION ===
def validar_usuario(username):
    if not (5 <= len(username) <= 15):
        return False
    if username[0].isdigit():
        return False
    if not username.isalnum() or not username.islower():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("python123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("123python") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("User_Name") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")