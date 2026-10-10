# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con ciertos criterios de seguridad utilizando condicionales e iteración: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un dígito numérico. Devuelve True si es válida y False en caso contrario.
# difficulty: Intermedio
# expected_output: False (para "abc1234")
# hint: Puedes iterar sobre cada carácter de la cadena usando un bucle 'for' y banderas lógicas o métodos de string como .isupper(), .islower() y .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_digito = True
            
        if tiene_mayuscula and tiene_minuscula and tiene_digito:
            return True
            
    return False

# === TESTS ===
try:
    assert validar_contrasena("Abc12345") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABCDEFGH") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")