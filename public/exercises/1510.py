# === METADATA ===
# title: Analizador y Validador de Nombre de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario y verifique si cumple con las siguientes reglas: 1) Longitud entre 5 y 15 caracteres (inclusive). 2) Solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales). La función debe devolver True si es válido y False en caso contrario.
# difficulty: Básico
# expected_output: True para "juan123", False para "Juan_123"
# hint: Utiliza los métodos de string como .islower(), .isalnum() y la función len() para verificar cada una de las condiciones.

# === SOLUTION ===
def validar_usuario(username):
    if 5 <= len(username) <= 15:
        if username.isalnum() and username.islower():
            return True
    return False

# === TESTS ===
try:
    assert validar_usuario("juan123") == True, "Error: el test 1 ha fallado."
    assert validar_usuario("Juan_123") == False, "Error: considera casos límites en tu lógica."
    assert validar_usuario("abc1") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")