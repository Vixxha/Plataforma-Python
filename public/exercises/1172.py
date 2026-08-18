# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplen con los siguientes criterios de seguridad: tener al menos 8 caracteres de longitud, contener al menos un dígito numérico y contener al menos una letra mayúscula. La iteración debe procesar cada contraseña aplicando estas condiciones lógicas.
# difficulty: Intermedio
# expected_output: ['Abc12345', 'Python2024']
# hint: Utiliza un bucle for para recorrer la lista, y los métodos de string como .isupper() y .isdigit() junto con operadores lógicos.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    seguras = []
    for password in lista_contraseñas:
        if len(password) >= 8:
            tiene_mayuscula = any(c.isupper() for c in password)
            tiene_digito = any(c.isdigit() for c in password)
            if tiene_mayuscula and tiene_digito:
                seguras.append(password)
    return seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Abc12345", "debil", "Python2024", "sinmayus1", "SOLONUMEROS123"]) == ["Abc12345", "Python2024", "SOLONUMEROS123"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corta1A", "exacta8A1", "12345678"]) == ["exacta8A1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["abc", "def", "ghi"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")