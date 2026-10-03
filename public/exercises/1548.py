# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una contraseña cumple con tres reglas básicas de seguridad: debe tener una longitud mínima de 8 caracteres, debe contener al menos un dígito numérico y debe incluir al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Básico
# expected_output: True para "Python123", False para "abc123"
# hint: Puedes iterar sobre cada carácter de la cadena usando un bucle 'for' y verificar condiciones con métodos como .isdigit() e .isupper().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_digito = False
    tiene_mayuscula = False
    
    for char in password:
        if char.isdigit():
            tiene_digito = True
        elif char.isupper():
            tiene_mayuscula = True
            
        if tiene_digito and tiene_mayuscula:
            return True
            
    return False

# === TESTS ===
try:
    assert validar_contrasena("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("PYTHONABC") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")