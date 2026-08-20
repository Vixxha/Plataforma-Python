# === METADATA ===
# title: Validador de Contraseñas y Suma de Dígitos
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y devuelva una nueva lista con aquellas contraseñas que cumplan con dos condiciones: tener una longitud de al menos 8 caracteres y que la suma de todos sus dígitos numéricos sea exactamente igual a un número objetivo dado.
# difficulty: Intermedio
# expected_output: ['Password123', 'Admin2024']
# hint: Usa un bucle 'for' para iterar sobre la lista de contraseñas, condicionales 'if' para verificar la longitud, y otro bucle interno o comprensión para extraer y sumar los dígitos usando 'str.isdigit()'.

# === SOLUTION ===
def filtrar_contraseñas(passwords, objetivo):
    resultado = []
    for pwd in passwords:
        if len(pwd) >= 8:
            suma_digitos = sum(int(char) for char in pwd if char.isdigit())
            if suma_digitos == objetivo:
                resultado.append(pwd)
    return resultado

# === TESTS ===
try:
    assert filtrar_contraseñas(["Pass123", "Password123", "Admin2024", "abc"], 6) == ["Password123", "Admin2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas(["corto", "12345678", "90"], 9) == ["12345678"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas(["Abcdefg1", "Xyz9999"], 1) == ["Abcdefg1"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")