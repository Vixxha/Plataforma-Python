# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con requisitos mínimos de seguridad: debe tener una longitud mínima de 8 caracteres, contener al menos un número y al menos una letra mayúscula. La función debe retornar True si cumple todo, o False en caso contrario.
# difficulty: Intermedio
# expected_output: Retorna True o False según corresponda.
# hint: Utiliza un ciclo para recorrer la cadena y métodos de strings como .isupper() y .isdigit(), combinados con condicionales.

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
    assert validar_contrasena("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_contrasena("python123") == False, "Error: considera casos límites en tu lógica."
    assert validar_contrasena("PYTH123") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")