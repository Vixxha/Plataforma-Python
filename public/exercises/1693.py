# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con requisitos mínimos de seguridad: debe tener una longitud de al menos 8 caracteres, contener al menos una letra mayúscula, al menos una letra minúscula y al menos un número. La función debe retornar True si es válida y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Abcdef12", False para "clave"
# hint: Puedes recorrer la cadena con un bucle for y usar métodos de string como .isupper(), .islower() y .isdigit().

# === SOLUTION ===
def validar_contrasena(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_minuscula and tiene_numero

# === TESTS ===
try:
    assert validar_contrasena("Abcdef12") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("clave") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("ABCDEF12") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")