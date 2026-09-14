# === METADATA ===
# title: Validador de Contraseñas y Suma de Dígitos
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y devuelva una lista con aquellas que son válidas. Una contraseña es válida si cumple con dos condiciones: tiene una longitud de al menos 8 caracteres y la suma de todos los dígitos numéricos contenidos en ella es mayor o igual a 10.
# difficulty: Intermedio
# expected_output: ['Pass1234567', 'Secure999Code']
# hint: Usa un bucle para recorrer cada contraseña, condicionales para validar la longitud, y otro bucle (o comprensión) para verificar y sumar los dígitos usando el método .isdigit().

# === SOLUTION ===
def filtrar_contraseñas(lista_passwords):
    validas = []
    for pwd in lista_passwords:
        if len(pwd) >= 8:
            suma_digitos = sum(int(char) for char in pwd if char.isdigit())
            if suma_digitos >= 10:
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas(["abc", "Pass1234567", "short1", "Secure999Code"]) == ["Pass1234567", "Secure999Code"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas(["12345678", "abcdefgh", "99999999"]) == ["12345678", "99999999"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas(["short", "123", "abc12345"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")