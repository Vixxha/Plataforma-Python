# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que: 1) Filtre los productos con stock mayor a 0, 2) Ordene el resultado por precio de forma ascendente y 3) Busque y devuelva el nombre del primer producto cuyo precio sea igual o superior a un valor mínimo dado. Si no existe, retorna None.
# difficulty: Intermedio
# expected_output: "Laptop"
# hint: Utiliza list comprehensions o filter para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y un bucle o next() para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    for p in ordenados:
        if p['precio'] >= precio_minimo:
            return p['nombre']
    return None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 5},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 2}
    ]
    assert procesar_inventario(inventario, 100) == "Monitor", "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 1000) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 10) == "Mouse", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")