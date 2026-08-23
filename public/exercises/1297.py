# === METADATA ===
# title: Gestión de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los primeros `n` productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento, y slicing para limitar la cantidad de resultados.

# === SOLUTION ===
def procesar_inventario(productos, n):
    productos_filtrados = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados[:n]]

# === TESTS ===
try:
    inventario = [
        {"nombre": "Mouse", "precio": 25.50, "stock": 10},
        {"nombre": "Laptop", "precio": 1200.00, "stock": 3},
        {"nombre": "Teclado", "precio": 45.00, "stock": 0},
        {"nombre": "Smartphone", "precio": 800.00, "stock": 5}
    ]
    
    assert procesar_inventario(inventario, 2) == ["Laptop", "Smartphone"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 1) == ["Laptop"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{"nombre": "Agotado", "precio": 100.0, "stock": 0}], 1) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")