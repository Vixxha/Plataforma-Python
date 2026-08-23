# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con reglas básicas de seguridad: debe tener al menos 8 caracteres, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python123", False para "clave"
# hint: Puedes iterar sobre los caracteres de la cadena usando un bucle o usar métodos como .isupper() y .isdigit() combinados con condicionales.

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
    assert validar_contrasena("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("clave") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("PROGRAMACION9") == True, "Error: el caso base falló."
    assert validar_contrasena("abc12345") == False, "Error: faltan mayúsculas."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")