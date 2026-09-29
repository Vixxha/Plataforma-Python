# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una cadena de texto cumple con los requisitos mínimos de seguridad para una contraseña: al menos 8 caracteres de longitud, al menos una letra minúscula, al menos una letra mayúscula y al menos un dígito numérico. La función debe retornar True si cumple con todo, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False
# hint: Puedes utilizar bucles para iterar sobre los caracteres y métodos de cadena como .islower(), .isupper() y .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_digito = False
    
    for char in password:
        if char.islower():
            tiene_minuscula = True
        elif char.isupper():
            tiene_mayuscula = True
        elif char.isdigit():
            tiene_digito = True
            
    return tiene_minuscula and tiene_mayuscula and tiene_digito

# === TESTS ===
try:
    assert validar_contrasena("Abc12345") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("Short1") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")