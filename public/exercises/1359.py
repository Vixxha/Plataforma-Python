# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una contraseña cumple con requisitos básicos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar True si cumple todo, o False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "corta1"
# hint: Puedes usar los métodos de string como .isupper() y .isdigit() junto con un bucle para recorrer los caracteres.

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
    assert validar_contrasena("corta1") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("TODOMAYUSCULAS1") == True, "Error: el caso base falló."
    assert validar_contrasena("nuevesincifras") == False, "Error: debe validar correctamente la ausencia de números."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")