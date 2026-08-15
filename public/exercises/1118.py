# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y devuelva una nueva lista con aquellas que cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Abc12345', 'Python2023']
# hint: Puedes recorrer la lista con un bucle for y usar métodos de cadena como .isupper(), .islower() y .isdigit() junto con condicionales para evaluar cada carácter.

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
    assert filtrar_contraseñas_seguras(["Abc12345", "deb", "Python2023", "SOLO_MAYUSCULAS"]) == ["Abc12345", "Python2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "todominusculas1", "TODOMAYUSCULAS1"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["12345678", "abcdefgh", "ABCDEFGH"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")