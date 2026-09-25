# === METADATA ===
# title: Validador de Formato de Nombre de Usuario
# description: Escribe una función que reciba un string con un nombre de usuario y valide si cumple con las siguientes reglas: debe tener entre 6 y 12 caracteres (inclusive), solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales), y debe empezar obligatoriamente con una letra. Retorna True si es válido y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "python3", False para "PyThon_3"
# hint: Puedes usar los métodos de string como .islower(), .isalnum() o verificar el primer carácter con indexación o con .isalpha().

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
    assert validar_usuario("PyThon_3") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("123user") == False, "Error: el caso base falló."
    assert validar_usuario("dev") == False, "Error: la longitud mínima no se está respetando."
    assert validar_usuario("programador12") == True, "Error: el test con 12 caracteres falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")