# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de cadenas (contraseñas) y devuelva una nueva lista únicamente con aquellas contraseñas que cumplan con los siguientes criterios: al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura9A']
# hint: Puedes utilizar métodos de strings como .isupper(), any() y verificar la longitud con len().

# === SOLUTION ===
def filtrar_contraseñas seguras(lista_passwords):
    passwords_validas = []
    for pwd in lista_passwords:
        if len(pwd) >= 8:
            tiene_mayuscula = any(c.isupper() for c in pwd)
            tiene_numero = any(c.isdigit() for c in pwd)
            if tiene_mayuscula and tiene_numero:
                passwords_validas.append(pwd)
    return passwords_validas

# === TESTS ===
try:
    assert filtrar_contraseñas seguras(["Password123", "deb", "sinmayus1", "SOLONUMEROS123", "Segura9A"]) == ["Password123", "Segura9A"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas seguras(["corto1A", "exacto8A1", "todominusculas"]) == ["exacto8A1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas seguras(["abc", "123", "ABC"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")