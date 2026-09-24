# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto que representa un nombre de usuario y verifique si cumple con las siguientes reglas: debe tener entre 5 y 15 caracteres (inclusive), solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales), y debe empezar obligatoriamente con una letra. Si cumple todas las condiciones, devuelve True; de lo contrario, devuelve False.
# difficulty: Intermedio
# expected_output: True para "usuario123", False para "123usuario"
# hint: Puedes usar los métodos de string como .islower(), .isalnum() y verificar el primer carácter con indexación, además de la función len().

# === SOLUTION ===
def validar_usuario(username):
    if not (5 <= len(username) <= 15):
        return False
    if not username[0].isalpha() or not username[0].islower():
        return False
    if not username.isalnum() or not username.islower():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("usuario123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("123usuario") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("abc") == False, "Error: el caso base falló."
    assert validar_usuario("usuario_valido") == False, "Error: no debe permitir guiones bajos."
    assert validar_usuario("dev2024") == True, "Error: debe validar correctamente combinaciones válidas."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")