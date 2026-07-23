# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'PyThOn2023']
# hint: Puedes usar métodos de string como .isupper(), .islower() y .isdigit() dentro de un bucle para evaluar cada carácter de la contraseña.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    contraseñas_validas = []
    for pwd in lista_contraseñas:
        if len(pwd) < 8:
            continue
        
        tiene_mayuscula = False
        tiene_minuscula = False
        tiene_numero = False
        
        for char in pwd:
            if char.isupper():
                tiene_mayuscula = True
            elif char.islower():
                tiene_minuscula = True
            elif char.isdigit():
                tiene_numero = True
                
        if tiene_mayuscula and tiene_minuscula and tiene_numero:
            contraseñas_validas.append(pwd)
            
    return contraseñas_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "short", "ALLCAPS", "12345678", "PyThOn2023"]) == ["Password123", "PyThOn2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc", "DEF", "123", "no_numbers_HERE"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Secure1Pass", "weakpass"]) == ["Secure1Pass"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")