# === METADATA ===
# title: Validador de Formato de Correo y Extracción de Dominio
# description: Escribe una función que reciba una dirección de correo electrónico como string. La función debe verificar si el correo contiene exactamente un símbolo '@' y al menos un punto '.' después del '@'. Si es válido, debe retornar un string con el dominio en minúsculas. Si no es válido, debe retornar el mensaje "Correo inválido".
# difficulty: Intermedio
# expected_output: "gmail.com"
# hint: Utiliza los métodos de string como `.count()`, `.find()` y rebanado (slicing) o `.split()`.

# === SOLUTION ===
def validar_y_extraer_dominio(correo):
    if correo.count('@') != 1:
        return "Correo inválido"
    
    usuario, dominio = correo.split('@')
    
    if not usuario or not dominio or '.' not in dominio:
        return "Correo inválido"
        
    if dominio.startswith('.') or dominio.endswith('.'):
        return "Correo inválido"
        
    return dominio.lower()

# === TESTS ===
try:
    assert validar_y_extraer_dominio("Usuario@Gmail.com") == "gmail.com", "Error: el test 1 ha fallado."
    assert validar_y_extraer_dominio("test.correo@u-temuco.cl") == "u-temuco.cl", "Error: considera casos límites en tu lógica."
    assert validar_y_extraer_dominio("correo-invalido@dominio") == "Correo inválido", "Error: el caso base falló."
    assert validar_y_extraer_dominio("sinarroba.com") == "Correo inválido", "Error: faltó validar la presencia del '@'."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")