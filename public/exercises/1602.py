# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una contraseña cumple con criterios básicos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python123", False para "debil"
# hint: Puedes recorrer la cadena usando un bucle o iteración para verificar cada carácter, utilizando funciones como .isupper() y .isdigit(), además de len() para la longitud.

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_digito = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_digito = True
            
    return tiene_mayuscula and tiene_digito

# === TESTS ===
try:
    assert validar_contrasena("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("debil") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("SOLOMAYUSCULAS1") == True, "Error: el caso base falló."
    assert validar_contrasena("sinmayusculas1") == False, "Error: verifica la validación de letras mayúsculas."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")