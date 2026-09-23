# === METADATA ===
# title: Analizador de Facturación y Descuentos
# description: Escribe una función que procese una lista de precios de productos y un código de membresía. Aplica la lógica de iteración para sumar los precios y aplica condiciones según la membresía: 'VIP' descuenta un 20%, 'Socio' un 10%, y 'Normal' sin descuento. Si el total acumulado sin descuento supera los 500, aplica un 5% adicional de descuento por volumen (aplicado después del descuento de membresía). Retorna el precio final redondeado a 2 decimales.
# difficulty: Intermedio
# expected_output: 342.0
# hint: Usa un bucle 'for' para sumar los precios, luego aplica la estructura condicional (if-elif-else) para el descuento por membresía, y finalmente verifica si el subtotal supera 500 para el descuento por volumen.

# === SOLUTION ===
def calcular_total_factura(precios, membresia):
    subtotal = sum(precios)
    
    if membresia == "VIP":
        total = subtotal * 0.80
    elif membresia == "Socio":
        total = subtotal * 0.90
    else:
        total = subtotal
        
    if subtotal > 500:
        total = total * 0.95
        
    return round(total, 2)

# === TESTS ===
try:
    assert calcular_total_factura([100, 200, 250], "VIP") == 427.5, "Error: el test 1 ha fallado."
    assert calcular_total_factura([50, 50], "Normal") == 100.0, "Error: considera casos límites en tu lógica."
    assert calcular_total_factura([300, 300], "Socio") == 513.0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")