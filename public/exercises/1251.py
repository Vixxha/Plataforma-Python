# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con reglas básicas de seguridad: debe tener una longitud mínima de 8 caracteres, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python123", False para "python"
# hint: Puedes usar bucles para iterar sobre los caracteres de la cadena y métodos como .isupper() o .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_digito = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_digito = True
            
    return tiene_mayuscula and tiene_digito

# === TESTS ===
try:
    assert validar_contrasena("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("python") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("PYTHONDOWN") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")