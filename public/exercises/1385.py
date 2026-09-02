# === METADATA ===
# title: Validador de Contraseña Segura con Intentos
# description: Escribe una función que reciba una lista de intentos de contraseña y devuelva cuántas de ellas cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos un dígito numérico y al menos una letra mayúscula. La iteración debe detenerse inmediatamente si se encuentra una contraseña que sea "ADMIN_BYPASS", devolviendo el texto "Acceso de Emergencia".
# difficulty: Intermedio
# expected_output: 2 (para una lista donde 2 contraseñas son válidas y no hay bypass) o "Acceso de Emergencia" si aparece el bypass.
# hint: Usa un bucle 'for' para iterar sobre la lista y condiciones 'if' para evaluar cada criterio. Recuerda usar métodos de string como .isupper() y .isdigit().

# === SOLUTION ===
def validar_contraseñas(intentos):
    validas = 0
    for pwd in intentos:
        if pwd == "ADMIN_BYPASS":
            return "Acceso de Emergencia"
        
        tiene_longitud = len(pwd) >= 8
        tiene_mayuscula = any(c.isupper() for c in pwd)
        tiene_digito = any(c.isdigit() for c in pwd)
        
        if tiene_longitud and tiene_mayuscula and tiene_digito:
            validas += 1
            
    return validas

# === TESTS ===
try:
    assert validar_contraseñas(["Pass1234", "short", "ALLCAPS1", "ADMIN_BYPASS"]) == "Acceso de Emergencia", "Error: el test 1 ha fallado."
    assert validar_contraseñas(["ClaveSegura1", "12345678", "abc", "A1b2C3d4"]) == 2, "Error: considera casos límites en tu lógica."
    assert validar_contraseñas(["solominusculas", "12345678", "TODOMAYUSCULAS"]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")