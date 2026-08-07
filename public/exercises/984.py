# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos cuyo precio sea menor o igual a un presupuesto máximo, los ordene de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente busque y devuelva el nombre del producto que se encuentra en una posición específica (índice) del resultado filtrado y ordenado. Si el índice está fuera de rango, debe retornar None.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Puedes usar list comprehensions para filtrar, el método sort() o la función sorted() con claves múltiples para ordenar, y verificar el tamaño de la lista antes de acceder al índice.

# === SOLUTION ===
def procesar_y_buscar_producto(productos, presupuesto_maximo, indice_busqueda):
    filtrados = [p for p in productos if p['precio'] <= presupuesto_maximo]
    
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    if 0 <= indice_busqueda < len(ordenados):
        return ordenados[indice_busqueda]['nombre']
    return None

# === TESTS ===
try:
    inventario = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Audífonos", "precio": 45}
    ]
    
    assert procesar_y_buscar_producto(inventario, 50, 0) == "Audífonos", "Error: el test 1 ha fallado."
    assert procesar_y_buscar_producto(inventario, 50, 1) == "Mouse", "Error: considera casos límites en tu lógica."
    assert procesar_y_buscar_producto(inventario, 20, 0) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")