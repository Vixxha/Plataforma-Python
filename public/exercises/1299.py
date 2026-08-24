# === METADATA ===
# title: Filtrado, Búsqueda y Ordenamiento de Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre" y "precio"), un precio máximo para filtrar, y un término de búsqueda (subcadena) para el nombre. La función debe filtrar los productos cuyo precio sea menor o igual al máximo y cuyo nombre contenga el término de búsqueda (ignorando mayúsculas/minúsculas). Finalmente, debe retornar la lista resultante ordenada de menor a mayor precio. Si dos productos tienen el mismo precio, deben ordenarse alfabéticamente por su nombre.
# difficulty: Intermedio
# expected_output: [{'nombre': 'Teclado', 'precio': 45.5}, {'nombre': 'Mouse', 'precio': 25.0}]
# hint: Puedes usar list comprehensions o la función filter para aplicar las condiciones, y el método sorted() con una clave múltiple (lambda x: (x['precio'], x['nombre'])) para ordenar adecuadamente.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, precio_maximo, termino_busqueda):
    termino_busqueda = termino_busqueda.lower()
    
    # Filtrar
    filtrados = [
        p for p in productos 
        if p["precio"] <= precio_maximo and termino_busqueda in p["nombre"].lower()
    ]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x["precio"], x["nombre"]))
    
    return ordenados

# === TESTS ===
try:
    inventario = [
        {"nombre": "Laptop Pro", "precio": 1200.0},
        {"nombre": "Mouse Inalámbrico", "precio": 25.0},
        {"nombre": "Teclado Mecánico", "precio": 85.5},
        {"nombre": "Mouse Gamer", "precio": 45.0},
        {"nombre": "Monitor 24", "precio": 180.0}
    ]
    
    test1 = [
        {"nombre": "Mouse Inalámbrico", "precio": 25.0},
        {"nombre": "Mouse Gamer", "precio": 45.0}
    ]
    
    test2 = [
        {"nombre": "Mouse Inalámbrico", "precio": 25.0},
        {"nombre": "Teclado Mecánico", "precio": 85.5}
    ]
    
    test3 = []

    assert filtrar_y_ordenar_productos(inventario, 50.0, "mouse") == test1, "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 100.0, "o") == test2, "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 10.0, "laptop") == test3, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")