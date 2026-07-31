# === METADATA ===
# title: Validador de Nombre de Usuario
# description: Escribe una función que valide un nombre de usuario según las siguientes reglas: debe tener entre 5 y 12 caracteres de longitud (inclusive), contener únicamente letras y números (sin espacios ni símbolos especiales), y empezar obligatoriamente con una letra. La función debe retornar True si cumple todas las condiciones, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "py" (muy corto), False para "123user" (empieza con número).
# hint: Puedes usar métodos de string como .isalnum(), .isalpha(), len() y verificar el primer carácter con indexación.

# === SOLUTION ===
def validar_usuario(username):
    if not (5 <= len(username) <= 12):
        return False
    if not username[0].isalpha():
        return False
    if not username.isalnum():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("Python2023") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("py") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("123user") == False, "Error: el caso base falló."
    assert validar_usuario("User_Name") == False, "Error: los símbolos especiales no están permitidos."
    assert validar_usuario("A1b2C3d4") == True, "Error: el test de longitud y formato válido falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")