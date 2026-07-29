# === METADATA ===
# title: Validador y Formateador de Cadenas
# description: Escribe una función que tome una cadena de texto representando un nombre completo con espacios irregulares, elimine los espacios sobrantes al inicio y final, asegure que cada palabra comience con mayúscula (formato título) y devuelva las iniciales del nombre en mayúsculas separadas por puntos (ej. "Juan Carlos Pérez" -> "J.C.P."). Sin embargo, en lugar de retornar solo las iniciales, la función debe retornar un diccionario o string formateado. Mejor aún: retorna una tupla con (nombre_formateado, iniciales). Modifiquemos para simplificar: la función debe limpiar los espacios y retornar el string en formato título, pero añadiendo las iniciales entre paréntesis al final, por ejemplo: "Juan Carlos Pérez (J.C.P.)".
# difficulty: Intermedio
# expected_output: "Juan Carlos Pérez (J.C.P.)"
# hint: Puedes usar los métodos de string como `.strip()`, `.split()`, `.title()`, y unir las primeras letras de cada palabra usando una comprensión de lista.

# === SOLUTION ===
def formatear_nombre_con_iniciales(texto: str) -> str:
    # Limpiar espacios múltiples y extremos
    palabras = texto.strip().split()
    if not palabras:
        return ""
    
    # Formato título para cada palabra
    palabras_formateadas = [p.capitalize() for p in palabras]
    nombre_formateado = " ".join(palabras_formateadas)
    
    # Obtener iniciales
    iniciales = ".".join([p[0].upper() for p in palabras_formateadas]) + "."
    
    return f"{nombre_formateado} ({iniciales})"

# === TESTS ===
try:
    assert formatear_nombre_con_iniciales("  juan carlos pérez  ") == "Juan Carlos Pérez (J.C.P.)", "Error: el test 1 ha fallado."
    assert formatear_nombre_con_iniciales("ANTONIO  JOSÉ   GARCÍA") == "Antonio José García (A.J.G.)", "Error: considera casos límites en tu lógica."
    assert formatear_nombre_con_iniciales("marta") == "Marta (M.)", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")