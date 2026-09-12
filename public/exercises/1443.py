# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con ciertos criterios de seguridad usando bucles y condicionales: debe tener al menos 8 caracteres, contener al menos una letra mayúscula, una minúscula y un número. La función debe retornar True si es válida y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False según corresponda.
# hint: Puedes recorrer la cadena de texto carácter por carácter usando un bucle 'for' y banderas (variables booleanas) para verificar cada condición.

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
        
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_minuscula and tiene_numero

# === TESTS ===
try:
    assert validar_contrasena("Abc12345") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABC12345") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")