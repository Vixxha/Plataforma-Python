# === METADATA ===
# title: Validador de Nombres de Usuario y Capitalización
# description: Escribe una función que reciba una cadena con un nombre de usuario completo (nombre y apellido). La función debe limpiar los espacios sobrantes al inicio y al final, verificar que contenga exactamente dos palabras, y retornar el nombre formateado con la primera letra de cada palabra en mayúscula y el resto en minúsculas. Si la cadena no contiene exactamente dos palabras, debe retornar "Nombre inválido".
# difficulty: Intermedio
# expected_output: "Ana Maria"
# hint: Puedes usar los métodos de string como strip() y split() para separar las palabras, y el método title() o una combinación de capitalización para dar el formato correcto.

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    if not isinstance(nombre_completo, str):
        return "Nombre inválido"
    
    nombre_limpio = nombre_completo.strip()
    
    if not nombre_limpio:
        return "Nombre inválido"
        
    palabras = nombre_limpio.split()
    
    if len(palabras) != 2:
        return "Nombre inválido"
        
    palabras_formateadas = [palabra.capitalize() for palabra in palabras]
    
    return " ".join(palabras_formateadas)

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maría ") == "Ana María", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN PEREZ") == "Juan Perez", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("carlos") == "Nombre inválido", "Error: el caso base falló."
    assert formatear_nombre_usuario("maria jose perez") == "Nombre inválido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")