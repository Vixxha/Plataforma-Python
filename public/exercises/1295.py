# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a 0, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por su nombre) y finalmente retornar una lista únicamente con los nombres de los productos que cumplan con la condición de búsqueda de pertenecer a una categoría o precio menor a un límite dado, o simplemente retornar los nombres ordenados. Para este ejercicio, filtra los productos con stock > 0 y ordénalos por precio ascendente, devolviendo una lista con los nombres de los productos que cuesten menos o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la función 'filter' o una lista por comprensión para el filtrado, y la función 'sorted' con una clave compuesta (tupla) para el ordenamiento.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto_maximo):
    # Filtrar productos con stock > 0 y precio menor o igual al presupuesto
    productos_filtrados = [
        p for p in productos 
        if p['stock'] > 0 and p['precio'] <= presupuesto_maximo
    ]
    
    # Ordenar primero por precio (ascendente) y luego por nombre (alfabéticamente)
    productos_ordenados = sorted(
        productos_filtrados, 
        key=lambda x: (x['precio'], x['nombre'])
    )
    
    # Extraer únicamente los nombres
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 3},
        {'nombre': 'Audífonos', 'precio': 45, 'stock': 7}
    ]
    
    # Test 1: Presupuesto que incluye varios elementos, probando ordenamiento por precio y nombre (Teclado tiene stock 0, Audífonos y Teclado valen 45)
    assert filtrar_y_ordenar_productos(inventario, 100) == ['Mouse', 'Audífonos', 'Monitor'], "Error: el test 1 ha fallado."
    
    # Test 2: Presupuesto bajo donde solo algunos entran y se respeta el stock > 0
    assert filtrar_y_ordenar_productos(inventario, 30) == ['Mouse'], "Error: considera casos límites en tu lógica."
    
    # Test 3: Presupuesto donde ningún producto cumple la condición o el stock es 0
    assert filtrar_y_ordenar_productos(inventario, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")