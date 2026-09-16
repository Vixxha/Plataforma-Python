# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una lista de contraseñas cumple con ciertos criterios de seguridad básicos: debe tener al menos 8 caracteres, contener al menos un número y una letra mayúscula. La función debe retornar cuántas contraseñas de la lista son válidas.
# difficulty: Intermedio
# expected_output: 2
# hint: Utiliza un ciclo for para recorrer la lista, y los métodos isupper(), isdigit() de las cadenas junto con condicionales.

# === SOLUTION ===
def contar_contraseñas_validas(lista_contraseñas):
    validas = 0
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_num = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_num = True
            if tiene_mayus and tiene_num:
                validas += 1
    return validas

# === TESTS ===
try:
    assert contar_contraseñas_validas(["Password123", "abc", "NoNumberHere", "A1b"]) == 1, "Error: el test 1 ha fallado."
    assert contar_contraseñas_validas(["Segura1A", "OTRAClave9", "debil", "12345678"]) == 2, "Error: considera casos límites en tu lógica."
    assert contar_contraseñas_validas(["Short1A", "SuperLongPasswordWithoutNumber", "aB1"]) == 1, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")