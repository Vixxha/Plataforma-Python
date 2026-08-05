# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que reciba un string con un nombre de usuario y valide si cumple con los siguientes criterios: debe tener entre 6 y 12 caracteres (inclusive), solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales), y debe empezar obligatoriamente con una letra. Si cumple todo, devuelve True; de lo contrario, devuelve False.
# difficulty: Intermedio
# expected_output: True para "python3", False para "User_123"
# hint: Utiliza métodos de string como .isalnum(), .islower() y verifica las condiciones de longitud y el primer carácter usando índices.

# === SOLUTION ===
def validar_usuario(username: str) -> bool:
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
    assert validar_usuario("User_123") == Error_caso := False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("dev") == False, "Error: el caso base falló."
    assert validar_usuario("1234567") == False, "Error: el test 4 ha fallado."
except NameError:
    # Ajuste para el assert del test 2 usando una variable booleana directa
    pass

try:
    assert validar_usuario("python3") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("User_123") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("dev") == False, "Error: el caso base falló."
    assert validar_usuario("1234567") == False, "Error: el test 4 ha fallado."
    assert validar_usuario("programador") == True, "Error: el test 5 ha fallado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")