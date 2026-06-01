# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), debes filtrar los productos con stock mayor a cero, ordenarlos de menor a mayor precio y finalmente buscar el nombre del producto más barato que cumpla la condición. Si no hay productos, retorna None.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista resultante con sort() o sorted() usando una función lambda como llave, y finalmente accede al primer elemento.

# === SOLUTION ===
def buscar_producto_mas_economico(inventario):
    productos_disponibles = [p for p in inventario if p['stock'] > 0]
    if not productos_disponibles:
        return None
    
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return productos_ordenados[0]['nombre']

# === TESTS ===
try:
    inventario_test = [
        {"nombre": "Laptop", "precio": 1000, "stock": 5},
        {"nombre": "Mouse", "precio": 20, "stock": 0},
        {"nombre": "Teclado", "precio": 45, "stock": 10},
        {"nombre": "Monitor", "precio": 200, "stock": 2}
    ]
    assert buscar_producto_mas_economico(inventario_test) == "Teclado", "Error: el test 1 ha fallado."
    assert buscar_producto_mas_economico([]) == None, "Error: debe manejar listas vacías."
    assert buscar_producto_mas_economico([{"nombre": "Cable", "precio": 10, "stock": 0}]) == None, "Error: debe ignorar productos sin stock."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")