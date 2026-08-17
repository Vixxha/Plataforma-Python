# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una contraseña cumple con requisitos básicos de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un dígito numérico. Debe retornar True si cumple todo, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "corta1"
# hint: Utiliza bucles o métodos de cadenas de texto junto con condicionales para verificar cada regla de manera independiente.

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
    assert validar_contrasena("Python2023") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("corta1") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("SOLOMAYUSCULAS") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")