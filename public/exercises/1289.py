# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una contraseña cumple con tres reglas básicas: tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python123", False para "corta1"
# hint: Utiliza bucles o recorridos de cadenas junto con métodos como .isupper() y .isdigit() combinados con lógica condicional.

# === SOLUTION ===
def validar_password(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for char in password:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_numero = True
            
    return tiene_mayuscula and tiene_numero

# === TESTS ===
try:
    assert validar_password("Python123") == True, "Error: el test 1 ha fallado."
    assert validar_password("corta1") == False, "Error: considera casos límites en tu lógica."
    assert validar_password("todominusculas1") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")