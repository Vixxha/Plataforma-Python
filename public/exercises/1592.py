# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos un número y al menos un carácter especial (de entre @, #, $, %). La función debe retornar True si cumple todos los requisitos y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False según corresponda.
# hint: Utiliza un bucle para recorrer los caracteres de la cadena y emplea variables booleanas o contadores para verificar cada condición requerida.

# === SOLUTION ===
def validar_contrasena(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False
    caracteres_especiales = "@#$%";
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        elif char.isdigit():
            tiene_numero = True
        elif char in caracteres_especiales:
            tiene_especial = True
            
    return tiene_mayuscula and tiene_numero and tiene_especial

# === TESTS ===
try:
    assert validar_contrasena("Abcdef1@") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abcdef1@") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABCDEF1@") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")