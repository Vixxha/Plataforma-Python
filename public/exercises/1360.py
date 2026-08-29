# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con ciertos criterios básicos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula. La función debe retornar True si es válida y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False según corresponda.
# hint: Puedes utilizar bucles para iterar sobre los caracteres y métodos de cadena como .isupper() y .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_numero

# === TESTS ===
try:
    assert validar_contrasena("Abc12345") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABC12345") == True, "Error: el caso base falló."
    assert validar_contrasena("Short1") == False, "Error: la validación de longitud falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")