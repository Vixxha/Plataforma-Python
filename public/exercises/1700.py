# === METADATA ===
# title: Validador de Contraseñas Seguras y Contador de Intentos
# description: Escribe una función que reciba una lista de contraseñas y devuelva cuántas de ellas cumplen con los requisitos mínimos de seguridad: longitud mínima de 8 caracteres, al menos un número y al menos una letra mayúscula. Utiliza bucles y lógica condicional para evaluar cada contraseña.
# difficulty: Intermedio
# expected_output: 2
# hint: Puedes iterar sobre la lista y, para cada cadena, usar métodos como isupper(), isdigit() y len() combinados con un bucle o una bandera lógica.

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
    assert contar_contraseñas_seguras(["Password123", "abc", "VALIDA99", "sinnumero"]) == 2, "Error: el test 1 ha fallado."
    assert contar_contraseñas_seguras(["corta1A", "todominusculas1", "12345678"]) == 0, "Error: considera casos límites en tu lógica."
    assert contar_contraseñas_seguras([]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")