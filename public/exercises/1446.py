# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan stock mayor a cero, los ordene por precio de forma ascendente y finalmente busque y devuelva una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Audífonos']
# hint: Puedes usar list comprehensions o filter para filtrar, la función sorted con una función lambda para ordenar por precio, y luego extraer los nombres de los elementos que cumplan con la condición del presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 50, "stock": 0},
        {"nombre": "Audífonos", "precio": 40, "stock": 3}
    ]
    assert procesar_inventario(inv1, 50) == ["Mouse", "Audífonos"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Laptop", "precio": 1000, "stock": 2},
        {"nombre": "Tablet", "precio": 300, "stock": 4}
    ]
    assert procesar_inventario(inv2, 1500) == ["Tablet", "Laptop"], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {"nombre": "Camisa", "precio": 20, "stock": 0},
        {"nombre": "Pantalón", "precio": 40, "stock": 0}
    ]
    assert procesar_inventario(inv3, 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")