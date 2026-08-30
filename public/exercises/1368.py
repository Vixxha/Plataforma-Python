# === METADATA ===
# title: Validador de Contraseñas y Intentos
# description: Escribe una función que valide una contraseña ingresada iterando sobre una lista de intentos permitidos. Debe retornar el primer intento válido que cumpla con las condiciones: longitud mínima de 8 caracteres, al menos un número y al menos una letra mayúscula. Si ningún intento es válido, debe retornar "Acceso denegado".
# difficulty: Intermedio
# expected_output: "Clave2023"
# hint: Usa un bucle 'for' para recorrer los intentos y condicionales con métodos como 'isupper()' o 'any()' combinados con 'isdigit()'.

# === SOLUTION ===
def validar_intentos_password(intentos):
    for password in intentos:
        if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
            return password
    return "Acceso denegado"

# === TESTS ===
try:
    assert validar_intentos_password(["abc", "12345678", "Clave2023", "OTRACOSA"]) == "Clave2023", "Error: el test 1 ha fallado."
    assert validar_intentos_password(["corto1", "sinmayuscula1", "demasiadodebilde"]) == "Acceso denegado", "Error: considera casos límites en tu lógica."
    assert validar_intentos_password(["Segura1A", "otra"]) == "Segura1A", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")