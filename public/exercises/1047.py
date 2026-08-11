# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos un número y al menos una letra mayúscula.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2023']
# hint: Puedes iterar sobre la lista y usar métodos de string como .isupper() y .isdigit() junto con bucles y condicionales.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    contraseñas_validas = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_mayuscula = False
            tiene_numero = False
            for char in pwd:
                if char.isupper():
                    tiene_mayuscula = True
                if char.isdigit():
                    tiene_numero = True
            if tiene_mayuscula and tiene_numero:
                contraseñas_validas.append(pwd)
    return contraseñas_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "deb", "MAYUSCULAS", "12345678", "Segura2023"]) == ["Password123", "Segura2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "ninguna", "SOLOLETRAS", "987654321"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["A1b2C3d4"]) == ["A1b2C3d4"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")