# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una cadena de texto cumple con los requisitos mínimos de seguridad para una contraseña: al menos 8 caracteres de longitud, al menos una letra mayúscula y al menos un número. La función debe retornar True si cumple todos los requisitos y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "corta1"
# hint: Utiliza iteración para recorrer los caracteres y métodos de cadena como .isupper() y .isdigit().

# === SOLUTION ===
def es_contrasena_segura(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_numero

# === TESTS ===
try:
    assert es_contrasena_segura("Python2023") == True, "Error: el test 1 ha fallado."
    assert es_contrasena_segura("corta1") == False, "Error: considera casos límites en tu lógica."
    assert es_contrasena_segura("SOLOMAYUSCULAS") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")