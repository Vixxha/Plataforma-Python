# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que reciba una cadena de texto representando una contraseña y verifique si cumple con las siguientes reglas: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un dígito numérico. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Password123", False para "clave"
# hint: Puedes recorrer la contraseña usando un bucle o iteración, y utilizar banderas (variables booleanas) junto con métodos de cadenas como .isupper(), .islower() y .isdigit().

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
            
    return tiene_mayuscula and tiene_minuscula and tiene_digito

# === TESTS ===
try:
    assert validar_contrasena("Password123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("clave") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("SOLOMAYUSCULAS1") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")