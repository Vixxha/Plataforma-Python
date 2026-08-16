# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan los siguientes criterios: tengan una longitud mínima de 8 caracteres, contengan al menos un número y no incluyan la palabra prohibida "password".
# difficulty: Intermedio
# expected_output: ['Abc12345', 'Secure99!']
# hint: Usa un bucle para iterar sobre cada contraseña, y métodos de strings como len(), any(c.isdigit() for c in s) y el operador 'in'.

# === SOLUTION ===
def filtrar_contraseñas(lista_contraseñas):
    validas = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8 and any(c.isdigit() for c in pwd) and "password" not in pwd.lower():
            validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas(["corto1", "Abc12345", "password123", "Secure99!"]) == ["Abc12345", "Secure99!"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas(["solo_letras", "12345678", "Passw0rd"]) == ["Passw0rd"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas(["abc", "123", ""]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")