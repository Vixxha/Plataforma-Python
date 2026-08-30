# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con ciertos criterios básicos de seguridad: debe tener al menos 8 caracteres de longitud, contener al menos un número y no puede estar compuesta solo por espacios en blanco. La función debe retornar True si es válida y False en caso contrario.
# difficulty: Intermedio
# expected_output: True (para "Pass1234"), False (para "abc")
# hint: Utiliza bucles o métodos de cadenas como .isdigit(), .isspace() y la función len() combinados con lógica condicional.

# === SOLUTION ===
def validar_contrasena(password):
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
        
    if password.isspace() or password == "":
        return False
        
    tiene_numero = False
    for char in password:
        if char.isdigit():
            tiene_numero = True
            break
            
    return tiene_numero

# === TESTS ===
try:
    assert validar_contrasena("Pass1234") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("        ") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")