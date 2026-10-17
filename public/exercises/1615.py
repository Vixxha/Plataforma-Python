# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con requisitos básicos de seguridad: debe tener una longitud mínima de 8 caracteres, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Password1", False para "pwd"
# hint: Utiliza bucles o métodos de cadena como .isupper() e .isdigit() combinados con iteración para verificar cada carácter.

# === SOLUTION ===
def es_contrasena_segura(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_digito = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_digito = True
            
        if tiene_mayuscula and tiene_digito:
            return True
            
    return False

# === TESTS ===
try:
    assert es_contrasena_segura("Password1") == True, "Error: el test 1 ha fallado."
    assert es_contrasena_segura("pwd") == False, "Error: considera casos límites en tu lógica."
    assert es_contrasena_segura("alllowercase1") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")