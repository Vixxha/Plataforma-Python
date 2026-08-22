# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma descendente según su precio (y alfabética ascendente por nombre en caso de empate) y finalmente busque y devuelva una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Utiliza list comprehensions o filter para filtrar, la función sorted con una clave múltiple (tupla) para ordenar, y asegúrate de aplicar correctamente el límite de precio en la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar productos con stock mayor a 0
    en_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio descendente (-p['precio']) y por nombre ascendente (p['nombre'])
    ordenados = sorted(en_stock, key=lambda x: (-x['precio'], x['nombre']))
    
    # Filtrar por precio menor o igual al límite y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= limite_precio]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 3},
        {'nombre': 'Audífonos', 'precio': 50, 'stock': 7}
    ]
    
    # Stock > 0: Laptop(1200), Mouse(25), Monitor(200), Audífonos(50)
    # Ordenados por precio desc, nombre asc:
    # 1. Laptop (1200)
    # 2. Monitor (200)
    # 3. Audífonos (50)
    # 4. Mouse (25)
    # Con limite_precio = 100, se seleccionan: Audífonos (50) y Mouse (25).
    # Orden final con limite <= 100: Audífonos y Mouse (ordenados por precio desc -> Audífonos(50) y Mouse(25))
    
    assert procesar_inventario(inventario_prueba, 100) == ['Audífonos', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 1500) == ['Laptop', 'Monitor', 'Audífonos', 'Mouse'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_prueba, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")