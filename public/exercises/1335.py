# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que tome una cadena que representa un nombre de usuario y verifique si cumple con las siguientes reglas: debe tener entre 5 y 12 caracteres (inclusive), solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales), y debe comenzar obligatoriamente con una letra. Si cumple todo, retorna True; de lo contrario, retorna False.
# difficulty: Intermedio
# expected_output: True para "usuario123", False para "User_1"
# hint: Puedes usar los métodos de string como .isalnum(), .islower(), .isalpha() y la función len().

# === SOLUTION ===
def validar_usuario(username):
    if not (5 <= len(username) <= 12):
        return False
    if not username[0].isalpha():
        return False
    if not username.isalnum() or not username.islower():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("usuario123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("User_1") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("123abc") == False, "Error: el caso base falló."
    assert validar_usuario("dev") == False, "Error: el test de longitud mínima falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")