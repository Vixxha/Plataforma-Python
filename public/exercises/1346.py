# === METADATA ===
# title: Validador de Nombre de Usuario
# description: Escribe una función que valide un nombre de usuario según las siguientes reglas: debe tener entre 6 y 12 caracteres de longitud (inclusive), solo puede contener letras minúsculas y números, y debe comenzar obligatoriamente con una letra. Retorna True si cumple todas las condiciones, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "usuario123", False para "User_12", False para "123user", False para "abc"
# hint: Recuerda utilizar los métodos de string como isalnum() y islower(), así como verificar el primer carácter y la longitud de la cadena.

# === SOLUTION ===
def validar_usuario(nombre):
    if not (6 <= len(nombre) <= 12):
        return False
    if not nombre[0].isalpha() or not nombre[0].islower():
        return False
    if not nombre.isalnum() or not nombre.islower():
        return False
    return True

# === TESTS ===
try:
    assert validar_usuario("usuario123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("User_12") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("123user") == False, "Error: el caso base falló."
    assert validar_usuario("abc") == False, "Error: verifica la validación de longitud mínima."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")