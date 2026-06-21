# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio, y finalmente devuelva el nombre del primer producto encontrado cuyo precio sea menor o igual a un presupuesto dado. Si no hay productos, devuelve None.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Utiliza el método .sort() o la función sorted() con una expresión lambda para ordenar por clave, y un bucle o filtro para buscar el producto adecuado.

# === SOLUTION ===
def buscar_producto_asequible(inventario, presupuesto):
    # Filtrar productos con stock > 0
    disponibles = [p for p in inventario if p['stock'] > 0]
    
    # Ordenar por precio de menor a mayor
    disponibles.sort(key=lambda x: x['precio'])
    
    # Buscar el primer producto que cumpla con el presupuesto
    for producto in disponibles:
        if producto['precio'] <= presupuesto:
            return producto['nombre']
            
    return None

# === TESTS ===
try:
    inventario_test = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 0}
    ]
    assert buscar_producto_asequible(inventario_test, 60) == 'Mouse', "Error: El test 1 ha fallado."
    assert buscar_producto_asequible(inventario_test, 10) == None, "Error: Debería retornar None si no hay presupuesto suficiente."
    assert buscar_producto_asequible([], 100) == None, "Error: El caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")