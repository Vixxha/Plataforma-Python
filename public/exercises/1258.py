# === METADATA ===
# title: Validador de Contraseñas Seguras y Cómputo de Intentos
# description: Escribe una función que reciba una lista de contraseñas y devuelva cuántas de ellas cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos un número y al menos una letra mayúscula. La iteración debe detenerse inmediatamente si se encuentra la palabra clave "BLOQUEAR" dentro de la lista de contraseñas.
# difficulty: Intermedio
# expected_output: 2
# hint: Usa un bucle 'for' junto con condicionales para validar cada regla y 'break' para interrumpir el ciclo si aparece la palabra "BLOQUEAR".

# === SOLUTION ===
def validar_lote_contraseñas(lista_passwords):
    validas = 0
    for pwd in lista_passwords:
        if pwd == "BLOQUEAR":
            break
        
        tiene_longitud = len(pwd) >= 8
        tiene_numero = any(c.isdigit() for c in pwd)
        tiene_mayuscula = any(c.isupper() for c in pwd)
        
        if tiene_longitud and tiene_numero and tiene_mayuscula:
            validas += 1
            
    return validas

# === TESTS ===
try:
    assert validar_lote_contraseñas(["Abc12345", "debil", "XyZ99999", "BLOQUEAR", "A1b2C3d4"]) == 2, "Error: el test 1 ha fallado."
    assert validar_lote_contraseñas(["corto1A", "sololetras", "12345678", "ABCDEFGH1"]) == 1, "Error: considera casos límites en tu lógica."
    assert validar_lote_contraseñas(["BLOQUEAR", "Password123"]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")