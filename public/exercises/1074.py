# === METADATA ===
# title: Validador y Formateador de Nombres de Usuario
# description: Escribe una función que tome el nombre completo de un usuario en formato de cadena (string), elimine los espacios sobrantes al inicio y al final, ponga la primera letra de cada palabra en mayúscula (formato título) y reemplace los espacios internos por guiones bajos (_).
# difficulty: Intermedio
# expected_output: "Ana_María_Gómez"
# hint: Puedes usar los métodos de string como strip(), title() y split()/join() para procesar el texto paso a paso.

# === SOLUTION ===
def formatear_nombre_usuario(nombre_completo):
    # Limpiamos espacios extremos, convertimos a formato título y unimos con guiones bajos
    palabras = nombre_completo.strip().split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return "_".join(palabras_capitalizadas)

# === TESTS ===
try:
    assert formatear_nombre_usuario("  ana maría gómez  ") == "Ana_María_Gómez", "Error: el test 1 ha fallado."
    assert formatear_nombre_usuario("JUAN CARLOS") == "Juan_Carlos", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_usuario("pedro") == "Pedro", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")