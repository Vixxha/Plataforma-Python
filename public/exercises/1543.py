# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista con los nombres de los primeros N productos resultantes (donde N es un parámetro dado). Si hay productos con el mismo precio, mantén su orden relativo original o usa el nombre como criterio secundario si es necesario.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar la función `filter` o listas por comprensión para filtrar, `sorted` con una función `key` personalizada para ordenar, y rebanado de listas (slicing) para limitar el resultado.

# === SOLUTION ===
def procesar_inventario(productos, n):
    filtrados = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    nombres = [p['nombre'] for p in ordenados[:n]]
    return nombres

# === TESTS ===
try:
    inventario_prueba = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 10},
        {"nombre": "Laptop", "precio": 1200.0, "stock": 5},
        {"nombre": "Teclado", "precio": 45.0, "stock": 0},
        {"nombre": "Smartphone", "precio": 800.0, "stock": 3},
        {"nombre": "Monitor", "precio": 300.0, "stock": 2}
    ]
    
    assert procesar_inventario(inventario_prueba, 2) == ["Laptop", "Smartphone"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 1) == ["Laptop"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")