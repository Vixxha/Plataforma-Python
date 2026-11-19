# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con criterios básicos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: False para "abc123", True para "Abcdefg1"
# hint: Utiliza bucles o métodos de cadenas como .isupper() y .isdigit() junto con condicionales.

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_numero

# === TESTS ===
try:
    assert validar_contrasena("abc123") == False, "Error: el test 1 ha fallado."
    assert validar_contrasena("Abcdefg1") == True, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABCDEFGH") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")