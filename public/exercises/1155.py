# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplan con los siguientes criterios: al menos 8 caracteres de longitud, al menos un número y al menos una letra mayúscula. La iteración debe procesar cada contraseña y la lógica condicional debe validar cada regla.
# difficulty: Intermedio
# expected_output: ['Password123', 'SecurePass9']
# hint: Utiliza métodos de strings como isupper(), any() con generadores, o recorre los caracteres con bucles for combinados con condicionales if.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    passar_filtro = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_numero = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_numero = True
            if tiene_mayus and tiene_numero:
                passar_filtro.append(pwd)
    return passar_filtro

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "weak", "SHORT1", "SecurePass9"]) == ["Password123", "SecurePass9"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc12345", "ABC12345", "aB1"]) == ["ABC12345"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["todominusculas", "TODOMAYUSCULAS", "12345678"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")