# === METADATA ===
# title: Validador de Contraseñas Seguras y Contador de Intentos
# description: Escribe una función que valide contraseñas según las reglas: longitud mínima de 8 caracteres, al menos un número y al menos una letra mayúscula. La función debe recibir una lista de contraseñas y retornar cuántas de ellas cumplen con todos los requisitos. Utiliza iteración para recorrer la lista y lógica condicional para evaluar cada regla.
# difficulty: Intermedio
# expected_output: 2
# hint: Recuerda usar métodos de strings como isupper(), any() con generadores, o bucles tradicionales con banderas (booleans) junto a condicionales 'if'.

# === SOLUTION ===
def contar_contraseñas_seguras(lista_contraseñas):
    contador = 0
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
                contador += 1
    return contador

# === TESTS ===
try:
    assert contar_contraseñas_seguras(["Password123", "weak", "SHORT1", "AnotherValid9"]) == 2, "Error: el test 1 ha fallado."
    assert contar_contraseñas_seguras(["alllowercase1", "ALLUPPERCASE1", "nosnumbers"]) == 0, "Error: considera casos límites en tu lógica."
    assert contar_contraseñas_seguras(["P1abcdef", "LongPassWithoutNumber", "12345678", "Valid123"]) == 2, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")