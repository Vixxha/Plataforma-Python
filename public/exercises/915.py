# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplen con los siguientes criterios de seguridad: tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula.
# difficulty: Intermedio
# expected_output: ['Python123', 'Segura2024']
# hint: Puedes recorrer la lista con un bucle, y para cada contraseña evaluar su longitud con `len()` y verificar caracteres usando métodos como `.isdigit()` y `.isupper()` junto con iteración.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    contraseñas_validas = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_numero = False
            tiene_mayuscula = False
            for char in pwd:
                if char.isdigit():
                    tiene_numero = True
                if char.isupper():
                    tiene_mayuscula = True
            if tiene_numero and tiene_mayuscula:
                contraseñas_validas.append(pwd)
    return contraseñas_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Python123", "debil", "SINnumeros", "Segura2024", "abc1"]) == ["Python123", "Segura2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "solominusculas", "SOLOMAYUSCULAS1"]) == ["SOLOMAYUSCULAS1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")