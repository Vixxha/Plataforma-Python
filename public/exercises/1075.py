# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome una cadena de texto representando un nombre de usuario con espacios y mayúsculas desordenadas, y devuelva el nombre limpio (sin espacios al inicio ni al final, con todas las palabras en minúscula y los espacios internos reemplazados por guiones bajos '_'). Además, debe verificar que no tenga espacios vacíos en el medio y que su longitud sea de al menos 4 caracteres. Si no cumple estas condiciones, debe retornar "INVÁLIDO".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Utiliza métodos de strings como strip(), split(), join() y lower(), además de validar la longitud y la cantidad de elementos resultantes.

# === SOLUTION ===
def procesar_nombre_usuario(nombre: str) -> str:
    nombre_limpio = nombre.strip()
    
    if len(nombre_limpio) < 4:
        return "INVÁLIDO"
    
    partes = nombre_limpio.split()
    
    if len(partes) > 1:
        return "_".join(partes).lower()
    else:
        # Si es una sola palabra continua pero cumple la longitud
        return nombre_limpio.lower()

# === TESTS ===
try:
    assert procesar_nombre_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert procesar_nombre_usuario("Ana") == "INVÁLIDO", "Error: considera casos límites en tu lógica."
    assert procesar_nombre_usuario("PROGRAMADOR  PYTHON") == "programador_python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")