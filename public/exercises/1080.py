# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente y finalmente retornar una lista con los nombres de los productos que cumplan con una búsqueda por palabra clave (insensible a mayúsculas/minúsculas) dentro de su nombre. Si no se provee palabra clave, debe retornar todos los nombres filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar list comprehensions para filtrar, el método sorted() con una función lambda para ordenar por clave, y el operador 'in' junto a .lower() para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, busqueda=""):
    # Filtrar productos con stock > 0 y que coincidan con la búsqueda (si existe)
    filtrados = [
        p for p in productos 
        if p.get('stock', 0) > 0 and busqueda.lower() in p.get('nombre', '').lower()
    ]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_prueba = [
        {"nombre": "Zapatos", "precio": 45.50, "stock": 5},
        {"nombre": "Gorra", "precio": 12.00, "stock": 0},
        {"nombre": "Camisa", "precio": 20.00, "stock": 10},
        {"nombre": "Pantalón", "precio": 35.00, "stock": 2}
    ]
    
    assert procesar_inventario(inventario_prueba, "a") == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_prueba, "Reloj") == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")