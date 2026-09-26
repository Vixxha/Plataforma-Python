# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con requisitos mínimos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula. La función debe retornar True si cumple con todo, y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "corta1"
# hint: Utiliza bucles para recorrer los caracteres y métodos de cadena como .isupper() y .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_numero

# === TESTS ===
try:
    assert validar_contrasena("Python2023") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("corta1") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("SOLOSINNUMEROS") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")