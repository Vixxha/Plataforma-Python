# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número. La función debe retornar True si es válida y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False
# hint: Puedes recorrer la cadena usando un bucle 'for' junto con métodos de strings como .isupper(), .islower() y .isdigit().

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
    assert validar_contrasena("ABCDEF1") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")