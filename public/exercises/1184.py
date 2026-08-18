# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un dígito numérico.
# difficulty: Intermedio
# expected_output: ['P@ssw0rd', 'Secur3Pass']
# hint: Utiliza bucles para recorrer la lista, y métodos de cadenas como .isupper(), .islower() e .isdigit() combinados con lógica condicional para verificar cada carácter.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_passwords):
    passwords_validas = []
    
    for pwd in lista_passwords:
        if len(pwd) < 8:
            continue
            
        tiene_mayuscula = False
        tiene_minuscula = False
        tiene_digito = False
        
        for char in pwd:
            if char.isupper():
                tiene_mayuscula = True
            elif char.islower():
                tiene_minuscula = True
            elif char.isdigit():
                tiene_digito = True
                
        if tiene_mayuscula and tiene_minuscula and tiene_digito:
            passwords_validas.append(pwd)
            
    return passwords_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["P@ssw0rd", "short", "ALLCAPS", "12345678", "Secur3Pass"]) == ["P@ssw0rd", "Secur3Pass"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["weak", "NO_DIGITS", "no_caps_123", "N0_l0wer"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Abc12345"]) == ["Abc12345"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")