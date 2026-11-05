# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con requisitos mínimos de seguridad: al menos 8 caracteres de longitud, al menos una letra mayúscula y al menos un número. La función debe retornar True si cumple con todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "clave"
# hint: Utiliza bucles o métodos de iteración sobre strings combinados con condicionales y funciones como .isupper() y .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.isdigit():
            tiene_numero = True
            
        if tiene_mayuscula and tiene_numero:
            return True
            
    return False

# === TESTS ===
try:
    assert validar_contrasena("Python2023") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("clave") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("SOLOMAYUSCULAS1") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")