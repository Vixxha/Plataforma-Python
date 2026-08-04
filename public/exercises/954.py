# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos que tengan un precio menor o igual a un presupuesto máximo, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista con solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la función `filter` o listas de comprensión, el método `sort()` o la función `sorted()` con una tupla como clave de ordenamiento, y finalmente extraer los nombres.

# === SOLUTION ===
def filtrar_ordenar_productos(productos, presupuesto_maximo):
    filtrados = [p for p in productos if p['precio'] <= presupuesto_maximo]
    filtrados_ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in filtrados_ordenados]

# === TESTS ===
try:
    inventario = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Monitor", "precio": 250},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Mouse", "precio": 45},
        {"nombre": "Audífonos", "precio": 80}
    ]
    
    assert filtrar_ordenar_productos(inventario, 100) == ["Mouse", "Teclado", "Audífonos"], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_productos(inventario, 300) == ["Mouse", "Teclado", "Audífonos", "Monitor"], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_productos(inventario, 30) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")