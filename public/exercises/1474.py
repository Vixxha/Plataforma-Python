# === METADATA ===
# title: Validador de Formato de Correo y Dominio
# description: Escribe una función que reciba un string con un correo electrónico. Debe verificar que contenga exactamente un símbolo '@', que tenga al menos un carácter antes y después del '@', y que termine obligatoriamente con el dominio '.com'. Si cumple todas las condiciones, debe retornar True; de lo contrario, False.
# difficulty: Intermedio
# expected_output: True para "usuario@dominio.com", False para "usuario@dominio.org" o "usuariodominio.com"
# hint: Utiliza los métodos de strings como .count(), .endswith(), y realiza particiones o validaciones de longitud.

# === SOLUTION ===
def validar_correo(correo):
    if correo.count('@') != 1:
        return False
    
    if not correo.endswith('.com'):
        return False
    
    partes = correo.split('@')
    usuario = partes[0]
    dominio = partes[1]
    
    if len(usuario) == 0 or len(dominio) <= 4:  # 4 por '.com'
        return False
        
    return True

# === TESTS ===
try:
    assert validar_correo("test@empresa.com") == True, "Error: el test 1 ha fallado."
    assert validar_correo("usuario@dominio.org") == False, "Error: considera casos límites en tu lógica."
    assert validar_correo("@dominio.com") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")