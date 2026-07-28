# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos cuyo stock sea mayor a cero, ordenarlos por precio de menor a mayor y, finalmente, retornar una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar listas por comprensión o las funciones filter y sorted, combinándolas adecuadamente para aplicar el filtro de stock, el ordenamiento por precio y el filtro por presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de menor a mayor
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inv = [
        {'nombre': 'Carne', 'precio': 15.5, 'stock': 0},
        {'nombre': 'Pan', 'precio': 1.2, 'stock': 10},
        {'nombre': 'Leche', 'precio': 2.5, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 0.8, 'stock': 20},
        {'nombre': 'Queso', 'precio': 5.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inv, 3.0) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 1.0) == ['Manzana'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 20.0) == ['Manzana', 'Pan', 'Leche', 'Queso'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")