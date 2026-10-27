# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una lista de contraseñas cumple con ciertos criterios mínimos de seguridad: debe tener una longitud de al menos 8 caracteres, contener al menos un dígito numérico y al menos una letra mayúscula. La función debe retornar cuántas contraseñas de la lista son válidas.
# difficulty: Intermedio
# expected_output: 2
# hint: Puedes iterar sobre cada contraseña de la lista y usar métodos de cadenas como .isupper(), .isdigit() y len(), combinándolos con estructuras condicionales.

# === SOLUTION ===
def contar_contraseñas_seguras(contraseñas):
    validas = 0
    for pwd in contraseñas:
        if len(pwd) >= 8:
            tiene_mayus = any(c.isupper() for c in pwd)
            tiene_digito = any(c.isdigit() for c in pwd)
            if tiene_mayus and tiene_digito:
                validas += 1
    return validas

# === TESTS ===
try:
    assert contar_contraseñas_seguras(["Password123", "short", "ALLMAYUSCULAS1", "minusc123"]) == 2, "Error: el test 1 ha fallado."
    assert contar_contraseñas_seguras(["abc", "12345678", "abcdeF1"]) == 1, "Error: considera casos límites en tu lógica."
    assert contar_contraseñas_seguras(["demasiadocortasi1", "SinNumeroA", "CONNUMERO1"]) == 1, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")