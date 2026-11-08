# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por un guion bajo ("_"), y asegurar que solo contenga caracteres alfanuméricos y guiones bajos. Si contiene caracteres inválidos, debe retornar un mensaje de error "Nombre inválido".
# difficulty: Intermedio
# expected_output: "juan_perez_99"
# hint: Utiliza métodos de string como .strip(), .lower(), .replace() y verifica caracteres con .isalnum() o bucles.

# === SOLUTION ===
def formatear_usuario(username):
    if not isinstance(username, str):
        return "Nombre inválido"
    
    cleaned = username.strip().lower().replace(" ", "_")
    
    if not cleaned:
        return "Nombre inválido"
        
    for char in cleaned:
        if not (char.isalnum() or char == '_'):
            return "Nombre inválido"
            
    return cleaned

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez 99  ") == "juan_perez_99", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana.Maria!") == "Nombre inválido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PYTHON_dev") == "python_dev", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")