# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos cuyo stock sea mayor a 0, ordenarlos por precio de forma ascendente y finalmente buscar y devolver el nombre del primer producto que coincida con un precio máximo dado. Si ningún producto cumple con la condición de precio máximo después del filtro y ordenamiento, debe retornar una cadena indicando "No encontrado".
# difficulty: Intermedio
# expected_output: "Camiseta"
# hint: Puedes usar list comprehensions o filter para el filtro, sorted() con una función lambda para el ordenamiento, y un ciclo for o búsqueda lineal para encontrar el elemento deseado.

# === SOLUTION ===
def procesar_inventario(productos, precio_maximo):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Buscar el primer producto cuyo precio sea menor o igual al precio_maximo
    for producto in ordenados:
        if producto['precio'] <= precio_maximo:
            return producto['nombre']
            
    return "No encontrado"

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Zapatos", "precio": 50, "stock": 5},
        {"nombre": "Camiseta", "precio": 15, "stock": 10},
        {"nombre": "Gorra", "precio": 20, "stock": 0},
        {"nombre": "Pantalón", "precio": 30, "stock": 2}
    ]
    assert procesar_inventario(inv1, 25) == "Camiseta", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 10) == "No encontrado", "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 50) == "No encontrado", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")