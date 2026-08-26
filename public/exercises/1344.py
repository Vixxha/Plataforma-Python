# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con ciertos criterios básicos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todos los requisitos y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "python"
# hint: Puedes recorrer la cadena usando un ciclo `for` y evaluar cada carácter con métodos como `.isupper()` o `.isdigit()`.

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_digito = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_digito = True
            
    return tiene_mayuscula and tiene_digito

# === TESTS ===
try:
    assert validar_contrasena("Python2023") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("python") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("PYTHON123") == True, "Error: el caso base falló."
    assert validar_contrasena("Short1") == False, "Error: verifica la longitud mínima."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")