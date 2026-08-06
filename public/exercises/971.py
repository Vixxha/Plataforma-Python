# === METADATA ===
# title: Validador de Contraseñas Seguras y Cuentas de Intentos
# description: Escribe una función que valide una contraseña según reglas básicas de seguridad y permita un máximo de intentos simulados mediante una lista de cadenas. La función debe evaluar una lista de intentos de contraseña y retornar True si encuentra una contraseña válida antes de agotar 3 intentos consecutivos fallidos (o la lista), y False en caso contrario. Una contraseña se considera válida si tiene al menos 8 caracteres y contiene al menos un dígito numérico.
# difficulty: Intermedio
# expected_output: True
# hint: Usa un bucle 'for' o 'while' para iterar sobre los intentos, aplica condiciones para verificar la longitud y la presencia de números, y lleva un contador de intentos fallidos.

# === SOLUTION ===
def validar_intentos_password(intentos):
    intentos_fallidos_consecutivos = 0
    
    for pwd in intentos:
        if intentos_fallidos_consecutivos >= 3:
            return False
            
        # Validar longitud y presencia de al menos un dígito
        tiene_digito = any(c.isdigit() for c in pwd)
        if len(pwd) >= 8 and tiene_digito:
            return True
        else:
            intentos_fallidos_consecutivos += 1
            
    return False

# === TESTS ===
try:
    assert validar_intentos_password(["corto", "12345", "clave12345"]) == True, "Error: el test 1 ha fallado."
    assert validar_intentos_password(["abc", "def", "ghi", "clave12345"]) == False, "Error: considera casos límites en tu lógica."
    assert validar_intentos_password(["solo_letras", "otra_vez_letras", "nada", "valida123"]) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")