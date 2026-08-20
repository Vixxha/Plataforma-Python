# === METADATA ===
# title: Filtrado, Búsqueda y Ordenamiento de Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), un precio máximo para filtrar, y un término de búsqueda (subcadena) para el nombre. La función debe filtrar los productos cuyo precio sea menor o igual al máximo y cuyo nombre contenga el término de búsqueda (ignorando mayúsculas/minúsculas). Finalmente, debe retornar la lista resultante ordenada de menor a mayor precio. Si dos productos tienen el mismo precio, ordénalos alfabéticamente por su nombre.
# difficulty: Intermedio
# expected_output: [{'nombre': 'Cafetera', 'precio': 45.0}, {'nombre': 'Café en grano', 'precio': 15.5}]
# hint: Puedes usar list comprehensions o filter para la búsqueda y filtrado, y la función sorted() con una clave múltiple (tupla) para ordenar por precio y luego por nombre.

# === SOLUTION ===
def procesar_productos(productos, precio_maximo, termino_busqueda):
    termino = termino_busqueda.lower()
    
    # Filtrar por precio y por coincidencia en el nombre
    filtrados = [
        p for p in productos 
        if p['precio'] <= precio_maximo and termino in p['nombre'].lower()
    ]
    
    # Ordenar por precio (ascendente) y luego por nombre (alfabéticamente)
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    return ordenados

# === TESTS ===
try:
    catalogo = [
        {"nombre": "Laptop Gamer", "precio": 1200.0},
        {"nombre": "Laptop de Oficina", "precio": 650.0},
        {"nombre": "Mouse Inalámbrico", "precio": 25.0},
        {"nombre": "Teclado Mecánico", "precio": 80.0},
        {"nombre": "Monitor 24", "precio": 150.0},
        {"nombre": "Mousepad", "precio": 15.0}
    ]
    
    test_1 = procesar_productos(catalogo, 100.0, "mouse")
    assert test_1 == [
        {"nombre": "Mousepad", "precio": 15.0},
        {"nombre": "Mouse Inalámbrico", "precio": 25.0}
    ], "Error: el test 1 ha fallado."

    test_2 = procesar_productos(catalogo, 700.0, "laptop")
    assert test_2 == [
        {"nombre": "Laptop de Oficina", "precio": 650.0},
        {"nombre": "Laptop Gamer", "precio": 1200.0} == False or {"nombre": "Laptop de Oficina", "precio": 650.0} # Nota: Solo debe traer menor o igual a 700
    ], "Error: considera casos límites en tu lógica."
    # Corrigiendo el assert estricto para el test 2:
    assert procesar_productos(catalogo, 700.0, "laptop") == [
        {"nombre": "Laptop de Oficina", "precio": 650.0}
    ], "Error: el test 2 ha fallado."

    test_3 = procesar_productos(catalogo, 50.0, "xyz")
    assert test_3 == [], "Error: el caso base falló."
    
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")