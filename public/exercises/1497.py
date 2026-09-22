# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que reciba una cadena de texto representando un nombre de usuario. La función debe limpiar los espacios en blanco al inicio y al final, convertir todo el nombre a minúsculas, reemplazar cualquier espacio interno por guiones bajos (_) y eliminar cualquier carácter que no sea una letra, un número o un guion bajo. Finalmente, debe verificar si el resultado tiene una longitud de al menos 5 caracteres y un máximo de 15; si es válido, retorna el string formateado, de lo contrario retorna "Inálido".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Puedes usar los métodos strip(), lower(), replace() y isalnum(), o iterar sobre la cadena filtrando los caracteres permitidos.

# === SOLUTION ===
def formatear_usuario(username):
    # Limpiar espacios y convertir a minúsculas
    limpio = username.strip().lower()
    
    # Filtrar caracteres permitidos (letras, números, espacios y guiones bajos)
    filtrado = "".join([c if c.isalnum() or c.isspace() or c == '_' else '' for c in limpio])
    
    # Reemplazar espacios internos por guiones bajos
    formateado = filtrado.replace(' ', '_')
    
    # Validar longitud (entre 5 y 15 caracteres)
    if 5 <= len(formateado) <= 15:
        return formateado
    return "Inálido"

# === TESTS ===
try:
    assert formatear_usuario("  Juan Perez!  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert formatear_usuario("Ana") == "Inálido", "Error: considera casos límites en tu lógica."
    assert formatear_usuario("PyThOn_3.11") == "python_311", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")