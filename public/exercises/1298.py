# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario como un string, elimine los espacios sobrantes al inicio y al final, ponga en mayúscula la primera letra de cada palabra y devuelva el nombre formateado junto con un contador de las vocales (a, e, i, o, u, sin importar si son mayúsculas o minúsculas) que contiene el nombre. Debe retornar una tupla con el formato: (nombre_formateado, total_vocales).
# difficulty: Intermedio
# expected_output: ("Ana Maria Gomez", 7)
# hint: Utiliza los métodos de string como strip(), title() y recorre la cadena o usa un contador para verificar cada carácter frente a las vocales.

# === SOLUTION ===
def formatear_y_contar_usuario(nombre_completo):
    nombre_limpio = nombre_completo.strip()
    nombre_formateado = nombre_limpio.title()
    
    vocales = "aeiouAEIOU"
    contador_vocales = sum(1 for char in nombre_formateado if char in vocales)
    
    return (nombre_formateado, contador_vocales)

# === TESTS ===
try:
    assert formatear_y_contar_usuario("  ana maria gomez  ") == ("Ana Maria Gomez", 7), "Error: el test 1 ha fallado."
    assert formatear_y_contar_usuario("CARLOS PEREZ") == ("Carlos Perez", 4), "Error: considera casos límites en tu lógica."
    assert formatear_y_contar_usuario("  luis  ") == ("Luis", 2), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")