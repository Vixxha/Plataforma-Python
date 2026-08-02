# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena que representa un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por un guion bajo '_', convierta todo el texto a minúsculas y finalmente asegure que termine con el sufijo '_valido'. Si la cadena está vacía, debe retornar 'inv_valido'.
# difficulty: Intermedio
# expected_output: "juan_perez_valido"
# hint: Utiliza los métodos de string de Python como strip(), replace(), lower() y verifica la longitud antes de operar.

# === SOLUTION ===
def formatear_usuario(username):
    if not username or not username.strip():
        return "inv_valido"
    
    limpio = username.strip().lower()
    formateado = limpio.replace(" ", "_")
    
    if not formateado.endswith("_valido"):
        formateado += "_valido"
        
    return formateado

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez  ") == "juan_perez_valido", "Error: el test 1 ha fallado."
    assert formatear_usuario("MARIA GOMEZ") == "maria_gomez_valido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("") == "inv_valido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")