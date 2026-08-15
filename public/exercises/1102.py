# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una contraseña cumple con criterios básicos de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un dígito numérico. Debe retornar True si cumple con todo, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False
# hint: Puedes recorrer la cadena usando un bucle 'for' junto con condicionales y los métodos 'isupper()' y 'isdigit()'.

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
            
        # Si ya encontramos ambos, podemos salir antes del bucle
        if tiene_mayuscula and tiene_digito:
            return True
            
    return False

# === TESTS ===
try:
    assert validar_contrasena("Abc12345") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABCDEFGH") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")