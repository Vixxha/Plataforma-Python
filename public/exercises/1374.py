# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por su nombre) y finalmente buscar y retornar una lista con únicamente los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar la función `filter` o listas por comprensión para filtrar, el método `.sort()` o la función `sorted()` con claves múltiples para ordenar, y finalmente extraer los nombres con otra comprensión de lista.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_max):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    disponibles_ordenados = sorted(disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    nombres_filtrados = [p['nombre'] for p in disponibles_ordenados if p['precio'] <= presupuesto_max]
    
    return nombres_filtrados

# === TESTS ===
try:
    inventario_ejemplo = [
        {"nombre": "Zapatos", "precio": 50, "stock": 10},
        {"nombre": "Camisa", "precio": 20, "stock": 5},
        {"nombre": "Gorra", "precio": 15, "stock": 0},
        {"nombre": "Pantalón", "precio": 35, "stock": 2},
        {"nombre": "Abrigo", "precio": 100, "stock": 4}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 50) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 15) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_ejemplo, 200) == ['Camisa', 'Pantalón', 'Zapatos', 'Abrigo'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")