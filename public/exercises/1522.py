# === METADATA ===
# title: Validador de Contraseñas y Suma de Dígitos
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y devuelva cuántas de ellas son válidas. Una contraseña es válida si tiene al menos 8 caracteres, contiene al menos un dígito numérico y la suma de todos los dígitos encontrados dentro de esa contraseña es mayor o igual a 10.
# difficulty: Intermedio
# expected_output: 2
# hint: Puedes iterar sobre cada carácter de la cadena usando un bucle, verificar si es un dígito con el método `.isdigit()` y usar lógica condicional para acumular la suma y validar la longitud.

# === SOLUTION ===
def contar_contrasenias_validas(lista_passwords):
    validas = 0
    for pwd in lista_passwords:
        if len(pwd) < 8:
            continue
        
        tiene_digito = False
        suma_digitos = 0
        
        for char in pwd:
            if char.isdigit():
                tiene_digito = True
                suma_digitos += int(char)
                
        if tiene_digito and suma_digitos >= 10:
            validas += 1
            
    return validas

# === TESTS ===
try:
    assert contar_contrasenias_validas(["abc12345", "password99", "short1"]) == 1, "Error: el test 1 ha fallado."
    assert contar_contrasenias_validas(["abcde12345", "99999password", "12345678"]) == 2, "Error: considera casos límites en tu lógica."
    assert contar_contrasenias_validas(["a1b2c3d4e5", "abcdefgh", "123456789"]) == 1, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")