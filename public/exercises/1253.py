# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que tome un string que representa un nombre de usuario y verifique si cumple con las siguientes reglas: debe tener una longitud entre 6 y 12 caracteres (inclusive), solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales), y debe comenzar obligatoriamente con una letra. Si cumple todo, retorna True; de lo contrario, False.
# difficulty: Intermedio
# expected_output: True para "python3", False para "User_123"
# hint: Puedes usar los métodos de string como .isalnum(), .islower(), .isalpha() y la función len().

# === SOLUTION ===
def validar_usuario(username):
    if not (6 <= len(username) <= 12):
        return False
    if not username[0].isalpha() or not username[0].islower():
        return False
    if not username.isalnum() or not username.islower():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("python3") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("User_123") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("dev") == False, "Error: el caso base falló."
    assert validar_usuario("1234567") == False, "Error: debe empezar con letra."
    assert validar_usuario("programando") == True, "Error: falló con un string válido largo."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")