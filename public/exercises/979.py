# === METADATA ===
# title: Validador de Correos Básicos
# description: Escribe una función que reciba una cadena de texto y determine si es un correo electrónico válido a nivel básico. Se considerará válido si contiene exactamente un símbolo '@', al menos un punto '.' después del '@', y ni el nombre de usuario ni el dominio están vacíos.
# difficulty: Intermedio
# expected_output: True para "usuario@dominio.com", False para "correo_sin_arroba.com"
# hint: Utiliza los métodos de strings como `.count()`, `.find()` y `.split()` para verificar las condiciones paso a paso.

# === SOLUTION ===
def validar_correo(email):
    if email.count('@') != 1:
        return False
    
    usuario, dominio = email.split('@')
    
    if not usuario or not dominio:
        return False
        
    if '.' not in dominio:
        return False
        
    # El dominio no debe empezar ni terminar con un punto, y debe tener al menos un carácter antes y después del punto
    partes_dominio = dominio.split('.')
    for parte in partes_dominio:
        if not parte:
            return False
            
    return True

# === TESTS ===
try:
    assert validar_correo("test@example.com") == True, "Error: el test 1 ha fallado."
    assert validar_correo("usuario.nombre@dominio.co.uk") == True, "Error: considera casos límites en tu lógica."
    assert validar_correo("correo_sin_arroba.com") == False, "Error: el caso base falló."
    assert validar_correo("@dominio.com") == False, "Error: no debe permitir usuarios vacíos."
    assert validar_correo("usuario@com") == False, "Error: el dominio debe tener un formato válido con puntos."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")