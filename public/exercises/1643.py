# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios donde cada diccionario representa un producto con 'nombre', 'precio' y 'stock'. La función debe filtrar los productos cuyo stock sea mayor a 0, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente buscar y retornar únicamente una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Manzanas', 'Pan', 'Leche']
# hint: Puedes usar las funciones filter() o comprensiones de lista para filtrar, sorted() con una clave múltiple (tupla) para ordenar, y finalmente extraer los nombres de los elementos que cumplan con el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(en_stock, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Queso", "precio": 15.5, "stock": 5},
        {"nombre": "Leche", "precio": 3.0, "stock": 10},
        {"nombre": "Pan", "precio": 1.5, "stock": 0},
        {"nombre": "Manzanas", "precio": 2.0, "stock": 20},
        {"nombre": "Jugo", "precio": 3.0, "stock": 8}
    ]
    assert procesar_inventario(inv1, 5.0) == ['Manzanas', 'Jugo', 'Leche'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Laptop", "precio": 800.0, "stock": 2},
        {"nombre": "Mouse", "precio": 25.0, "stock": 15},
        {"nombre": "Teclado", "precio": 25.0, "stock": 0}
    ]
    assert procesar_inventario(inv2, 50.0) == ['Mouse'], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {"nombre": "A", "precio": 10.0, "stock": 5},
        {"nombre": "B", "precio": 5.0, "stock": 2}
    ]
    assert procesar_inventario(inv3, 2.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")