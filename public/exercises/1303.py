# === METADATA ===
# title: Validador de Contraseñas Seguras y Creador de Resumen
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto). La función debe iterar sobre la lista y aplicar lógica condicional para filtrar aquellas que cumplan con los siguientes requisitos de seguridad: tener al menos 8 caracteres de longitud, contener al menos un dígito y contener al menos una letra mayúscula. La función debe retornar una lista con las contraseñas válidas.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura99']
# hint: Puedes usar métodos de strings como len(), .isdigit(), .isupper() combinados con un bucle for y condicionales.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    validas = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_digito = any(c.isdigit() for c in pwd)
            tiene_mayuscula = any(c.isupper() for c in pwd)
            if tiene_digito and tiene_mayuscula:
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "debil", "SINnumero", "Segura99"]) == ["Password123", "Segura99"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corta1A", "12345678", "ABCdef1"]) == ["ABCdef1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["todominusculas", "MAYUSCULASSINNUMERO"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")