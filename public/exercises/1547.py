# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que evalúe si una cadena de texto cumple con los requisitos básicos de una contraseña segura: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. La función debe retornar True si cumple todas las condiciones y False en caso contrario.
# difficulty: Intermedio
# expected_output: True o False
# hint: Puedes recorrer la cadena usando un bucle 'for' junto con métodos de strings como .isupper() y .isdigit(), combinándolos con condicionales y contadores o banderas (booleans).

# === SOLUTION ===
def es_contrasena_segura(password):
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
    assert es_contrasena_segura("Abc12345") == True, "Error: el test 1 ha fallado."
    assert es_contrasena_segura("abc12345") == False, "Error: considera casos límites en tu lógica."
    assert es_contrasena_segura("ABCDEFGH") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")