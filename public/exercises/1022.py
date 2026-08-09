# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una contraseña cumple con criterios básicos de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número. La función debe retornar True si cumple todos los requisitos y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False dependiendo de si la cadena cumple las reglas.
# hint: Puedes recorrer la cadena con un bucle while o for, y usar métodos de string como .isupper(), .islower() y .isdigit() junto con condicionales.

# === SOLUTION ===
def validar_contrasena(password):
    if len(password) < 8:
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
            
        if tiene_mayuscula and tiene_minuscula and tiene_numero:
            return True
            
    return False

# === TESTS ===
try:
    assert validar_contrasena("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("PYTHON123") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")